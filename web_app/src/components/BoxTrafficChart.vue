<script setup>
import { ref } from 'vue';
import { Chart, registerables } from 'chart.js';
</script>

<template>
    <div>
        <canvas ref="chartRef" width="1500" height="600"></canvas>
    </div>
</template>

<script>

Chart.register(...registerables);

const chartRef = ref(null);
let chartInstance = null;

export default {
    props: {
        traffic_2GHz: {
            type: Array,
            required: true,
        },
        traffic_5GHz: {
            type: Array,
            required: true,
        },
        connected_stations: {
            type: Array,
            required: true,
        },
        stationsTraffic: { 
            type: Object, 
            required: true,
        },
        stations_colors: {
            type: Array,
            required: true,
        },
        timestamps: {
            type: Array,
            required: true,
        },
    },
    mounted() {
        console.log("in mounted BoxTrafficChart Vue");
        this.updateChart();
    },
    watch: {
        traffic_2GHz(newValue, oldValue) {
            this.updateChart();
        },
        traffic_5GHz(newValue, oldValue) {
            this.updateChart(); 
        },
        connected_stations(newValue, oldValue) {
            this.updateChart(); 
        },
        stationsTraffic(newValue, oldValue) {
            this.updateChart();
        },
        stations_colors(newValue, oldValue) {
            this.updateChart();
        },
        timestamps(newValue, oldValue) {
            this.updateChart();
        }
    },
    methods: {
        updateChart() {
            console.log(`Updating traffic Chart`);
            const ctx = chartRef.value.getContext('2d');


            // Extract timestamps 
            const timestamps_2GHz = this.extractTimestamps(this.traffic_2GHz);
            const timestamps_5GHz = this.extractTimestamps(this.traffic_5GHz);
            //const timestamps_stations_traffic = this.extractStationTimestamps();
            const formatedTimestamps = this.timestamps.map(date => date.substring(11, 22));
            
            // Calculate traffic data
            const { traffic2GHz, traffic5GHz, stationsTraffic } = this.calculateTrafficData(timestamps_2GHz, timestamps_5GHz);

            // Calculate total traffic
            const totalTraffic = this.calculateTotalTraffic(traffic2GHz, traffic5GHz);
  
            // Update datasets
            const datasets = this.createDatasets(traffic2GHz, traffic5GHz, totalTraffic, stationsTraffic);

            // Update the chart instance with new data
            if (chartInstance) {
                chartInstance.data.labels = formatedTimestamps; // Update labels
                chartInstance.data.datasets = datasets; // Update datasets

                chartInstance.update('none'); // Refresh the chart
                // chartInstance.destroy();
            } else {
                // Create the chart instance if it doesn't exist
                chartInstance = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: formatedTimestamps,
                        datasets: datasets,
                    },
                    options: {
                        responsive: true,
                        animation: false,
                        scales: {
                            x: {
                                title: {
                                    display: false,
                                    text: 'Timestamp'
                                },
                                ticks: {
                                    autoSkip: true,
                                    display: false,
                                    maxTicksLimit: 10,
                                    minRotation: 45,
                                    maxRotation: 90
                                },
                            },
                            y: {
                                title: {
                                    display: true,
                                    text: 'Traffic (Mbps)'
                                }
                            }
                        }
                    },
                });
            }
        },
        extractTimestamps(data) {
            return data.map(item => item.timestamp);
        },
        calculateTrafficData(timestamps_2GHz, timestamps_5GHz) {
            // Extract traffic data
            const rxData_2GHz = this.traffic_2GHz.map(item => item.rx_Mbps);
            const txData_2GHz = this.traffic_2GHz.map(item => item.tx_Mbps);
            const rxData_5GHz = this.traffic_5GHz.map(item => item.rx_Mbps);
            const txData_5GHz = this.traffic_5GHz.map(item => item.tx_Mbps);
            
            // Create traffic arrays
            const traffic2GHz = [];
            const traffic5GHz = [];
            const stationsTraffic = {};
            for (const station of this.connected_stations) {
                stationsTraffic[station] = [];
            }

            // Process traffic data
            this.timestamps.forEach((timestamp) => {
                this.processTrafficData(timestamp, timestamps_2GHz, rxData_2GHz, txData_2GHz, traffic2GHz);
                this.processTrafficData(timestamp, timestamps_5GHz, rxData_5GHz, txData_5GHz, traffic5GHz);
                this.processStationTrafficData(timestamp, stationsTraffic);
            });

            return { traffic2GHz, traffic5GHz, stationsTraffic };
        },
        processTrafficData(timestamp, timestamps, rxData, txData, trafficArray) {
            // Check if timestamp is present in timestamps array
            const idx = timestamps.indexOf(timestamp);
            if (idx !== -1) {
                // append traffic to array
                const sampleTraffic = rxData[idx] + txData[idx];
                trafficArray.push(sampleTraffic);
            } else {
                // if timestamp not present append null
                trafficArray.push(null);
            }
        },
        processStationTrafficData(timestamp, stationsTraffic) {
            // loop over connected stations
            for (const station of this.connected_stations) {
                // Check if timestamp is present in timestamps array
                const idx = this.stationsTraffic[station].findIndex(element => element.timestamp === timestamp);
                if (idx !== -1) {
                    // append traffic to array
                    const sampleTraffic = this.stationsTraffic[station][idx].rx_Mbps + this.stationsTraffic[station][idx].tx_Mbps;
                    stationsTraffic[station].push(sampleTraffic);
                } else {
                    // if timestamp not present append null
                    stationsTraffic[station].push(null);
                }
            }
        },
        calculateTotalTraffic(traffic2GHz, traffic5GHz) {
            return traffic2GHz.map((value, index) => value + (traffic5GHz[index] || 0));
        },
        createDatasets(traffic2GHz, traffic5GHz, totalTraffic, stationsTraffic) {
            // Create box traffic datasets
            const datasets = [
                this.createDataset('2.4GHz', traffic2GHz, 'rgba(75, 192, 192, 1)', 'rgba(75, 192, 192, 0.2)', false),
                this.createDataset('5GHz', traffic5GHz, 'rgba(255, 99, 132, 1)', 'rgba(255, 99, 132, 0.2)', true),
                this.createDataset('Total', totalTraffic, 'rgba(54, 162, 235, 1)', 'rgba(54, 162, 235, 0.2)', true),
            ];

            // Create stations traffic dataset
            for (const [index, station] of this.connected_stations.entries()) {
                const { borderColor, backgroundColor } = this.stations_colors[index];
                datasets.push(this.createDataset(station, stationsTraffic[station], borderColor, backgroundColor));
            }

            return datasets;
        },
        createDataset(label, data, borderColor, backgroundColor, hidden) {
            return {
                label,
                data,
                borderColor,
                backgroundColor,
                spanGaps: true,
                fill: false,
                hidden: hidden,
            };
        },
    }
}

</script>

<style scoped>
h2 {
    text-align: center;
}
</style>
