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
        stations_rtd: { 
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
        }
    },
    mounted() {
        console.log("in mounted StationsRtdChart Vue");
        this.updateChart();
    },
    watch: {
        stations_rtd(newValue, oldValue) {
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
            console.log(`Updating stations rtd Chart`);
            const ctx = chartRef.value.getContext('2d');

            // Format timestamps 
            const formatedTimestamps = this.timestamps.map(date => date.substring(11, 22));

            // initialize stations counters
            const stationsRtd = this.initializeStationsRtd();

            console.log("In updateChart");
            console.log(`stations:${Object.keys(stationsRtd)}`);

            // Fill stations rtd
            this.populateStationsRtd(stationsRtd);

            // Update datasets
            const datasets = this.createDatasets(stationsRtd);

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
                                    text: 'Station RTD'
                                }
                            }
                        }
                    },
                });
            }
        },
        initializeStationsRtd() {
            // Extract stations 
            const stations = Object.keys(this.stations_rtd);
            const stationsRtd = {};
            // Create counters
            for (const station of stations) {
                stationsRtd[station] = [];                
            }
            return stationsRtd;
        },
        populateStationsRtd(stationsRtd) {
            // Extract stations 
            const stations = Object.keys(this.stations_rtd);
           
            // loop over timestamps array
            this.timestamps.forEach((timestamp) => {
                // loop over stations
                for (const station of stations) {
                    console.log(`udating station: ${station}`);
                    // check if timestamp is present in station counters array
                    const idx = this.stations_rtd[station].findIndex(element => element.timestamp === timestamp);
                    console.log(`station: ${station} found in idx:${idx}`);
                    if (idx !== -1) {
                        // Append data to station rtd
                        stationsRtd[station].push(this.stations_rtd[station][idx].rtd);
                    } else {
                        // Append null values to station rtd
                        stationsRtd[station].push(null);
                    }
                }
            });

        },
        createDatasets(stationsRtd) {
            const datasets = [];       
            // Create stations traffic dataset
            const stations = Object.keys(this.stations_rtd);

            for (const station of stations) {
                const index = stations.indexOf(station);
                const { borderColor, backgroundColor } = this.stations_colors[index];
                datasets.push(this.createDataset(station, stationsRtd[station], borderColor, backgroundColor));
            }
            return datasets;
        },
        createDataset(label, data, borderColor, backgroundColor) {
            return {
                label,
                data,
                borderColor,
                backgroundColor,
                spanGaps: true,
                fill: false,
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
