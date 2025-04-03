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
        counters_2GHz: {
            type: Array,
            required: true,
        },  
        counters_5GHz: {
            type: Array,
            required: true,
        },  
        timestamps: {
            type: Array,
            required: true,
        },        
    },
    mounted() {
        console.log("in mounted BoxCountersChart Vue");
        this.updateChart();
    },
    watch: {
        counters_2GHz(newValue, oldValue) {
            this.updateChart();
        },
        counters_5GHz(newValue, oldValue) {
            this.updateChart(); 
        },
        timestamps(newValue, oldValue) {
            this.updateChart(); 
        },
    },
    methods: {
        updateChart() {
            console.log(`Updating box counters Chart`);
            const ctx = chartRef.value.getContext('2d');


            // Extract timestamps 
            const timestamps_2GHz = this.extractTimestamps(this.counters_2GHz);
            const timestamps_5GHz = this.extractTimestamps(this.counters_5GHz);

            // Format timestamps
            const formatedTimestamps = this.timestamps.map(date => date.substring(11, 22));

            // Initialize counters
            const counters2GHz = this.initializeCounters();
            const counters5GHz = this.initializeCounters();

            // Fill counters
            this.populateCounters(timestamps_2GHz, this.counters_2GHz, counters2GHz);
            this.populateCounters(timestamps_5GHz, this.counters_5GHz, counters5GHz);

            // Create datasets
            const datasets = this.createDatasets(counters2GHz, counters5GHz);        

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
                                    text: 'Counters'
                                }
                            }
                        }
                    },
                });
            }
        },
        extractTimestamps(counters) {
            return counters.map(item => item.timestamp);
        },
        initializeCounters() {
            return {
                bytesReceived: [],
                bytesSent: [],
                noise: [],
                load: [],
                freeTime: [],
                rxTime: [],
                vendorStats_glitch: [],
                obssTime: [],
                txTime: [],
                intTime: [],
                noise_air: [],
                packetsReceived: [],
                packetsSent: [],
                errorsReceived: [],
                errorsSent: [],
            };
        },
        populateCounters(timestamps, counters, targetCounters) {
            // loop over timestamps array
            this.timestamps.forEach((timestamp) => {
                // Check if timestamp is present in counter timestamps
                const idx = timestamps.indexOf(timestamp);
                if (idx !== -1) {
                    // extract sample
                    const sample = counters[idx];
                    // loop over counter keys
                    Object.keys(targetCounters).forEach(key => {
                        // append value to counter 
                        targetCounters[key].push(sample[key]);
                    });
                } else {
                    // Append null to counter
                    Object.keys(targetCounters).forEach(key => {
                        targetCounters[key].push(null);
                    });
                }
            });
        },
        createDatasets(counters2GHz, counters5GHz) {
            const datasets = [];

            // Crete colors dict
            const colors = {
                '2GHz': 'rgba(255, 99, 132, 1)',
                '5GHz': 'rgba(75, 192, 192, 1)',
            };
            // Loop over bands 
            for (const [band, counters] of Object.entries({ '2GHz': counters2GHz, '5GHz': counters5GHz })) {
                // Loop over counter keys
                for (const [key, data] of Object.entries(counters)) {
                    // Create dataset
                    datasets.push({
                        label: `${key} ${band}`,
                        data: data,
                        borderColor: colors[band],
                        backgroundColor: 'rgba(255, 99, 132, 0)',
                        spanGaps: true,
                        fill: true,
                        hidden: true,
                    });
                }
            }
            return datasets;
        },
    }
}

</script>

<style scoped>
h2 {
    text-align: center;
}
</style>
