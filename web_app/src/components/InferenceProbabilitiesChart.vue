<script setup>
import { ref } from 'vue';
import { Chart, registerables } from 'chart.js';
</script>

<template>
    <div>
        <canvas ref="chartRef" width="1500" height="400"></canvas>
    </div>
</template>

<script>

Chart.register(...registerables);

const chartRef = ref(null);
let chartInstance = null;

export default {
    props: {
        inferences: {
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
        console.log("in mounted InferenceProbabilitiesChart Vue");
        this.updateChart();
    },
    watch: {
        inferences(newValue, oldValue) {
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
            console.log(`Updating inferences probailities chart`);
            const ctx = chartRef.value.getContext('2d');


            // Extract timestamps 
            const formatedTimestamps = this.timestamps.map(date => date.substring(11, 22));
            
            
            // Create inferences dict
            const stations_inferences_probabilities_dict = this.createInferencesDict();       

            // Update datasets
            const datasets = this.updateDatasets(stations_inferences_probabilities_dict);

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
                                    text: 'Inferences Probabilities'
                                },
                                ticks: {
                                    autoSkip: false,
                                    maxTicksLimit: 5,                                    
                                },
                            }
                        }
                    },
                });
            }
        },
        createInferencesDict() {
            const stations_in_inferences = Object.keys(this.inferences);
            const stationsInferencesProbabilities = {};

            for (const station of Object.keys(this.inferences)) {
                stationsInferencesProbabilities[station] = [];
            }

            this.timestamps.forEach((timestamp) => {
                // Loop over connected stations
                for (const station of stations_in_inferences) {
                    const idx_in_array = this.inferences[station].findIndex(element => element.timestamp === timestamp);
                    if (idx_in_array !== -1) {
                        stationsInferencesProbabilities[station].push(this.inferences[station][idx_in_array].probability);
                    } else {
                        stationsInferencesProbabilities[station].push(null);
                    }
                }
            });

            // return inferences dict
            return stationsInferencesProbabilities;
        },
        updateDatasets(stationsInferencesProbabilities) {
            const stations_in_inferences = Object.keys(this.inferences);
            const datasets = [];
            // Iterate over the dictionary to populate datasets for connected stations
            for (const [index, station] of stations_in_inferences.entries()) {
                // get station color
                const {borderColor, backgroundColor} = this.stations_colors[index];                 
                datasets.push({
                    label: station,
                    data: stationsInferencesProbabilities[station],
                    borderColor: borderColor,
                    backgroundColor: backgroundColor,
                    spanGaps: true,
                    fill: false, 
                });
            }
            // return datasets created
            return datasets;
        }
    }
}

</script>

<style scoped>
h2 {
    text-align: center;
}
</style>
