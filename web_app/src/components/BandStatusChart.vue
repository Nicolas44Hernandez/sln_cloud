<script setup>
import { ref } from 'vue';
import { Chart, registerables } from 'chart.js';
</script>

<template>
    <div>
        <canvas ref="chartRefBands" width="2000" height="200"></canvas>
    </div>
</template>

<script>

Chart.register(...registerables);

const chartRefBands = ref(null);
let chartInstance = null;

export default {
    props: {
        band_status: {
            type: Array,
            required: true,
        },
        timestamps: {
            type: Array,
            required: true,
        },
    },
    mounted() {
    console.log("in mounted BandStatusCharts Vue");
    },
    watch: {
        band_status(newValue, oldValue) {
            this.updateChart(newValue); 
        },
        timestamps(newValue, oldValue) {
            this.updateChart(newValue); 
        }
    },
    methods: {
        updateChart() {
            console.log(`Updating band status Chart`);
            const ctx = chartRefBands.value.getContext('2d');

            // Clear previous chart if it exists
            if (chartInstance) {
                chartInstance.destroy();
            }
            // Exctract band status data
            const bandStatus = [];
            this.timestamps.forEach((timestamp) => {
                this.processBandStatusData(timestamp, bandStatus);
            });

            // Create band status int arrays
            const formatedTimestamps = this.timestamps.map(date => date.substring(11, 22));   

            chartInstance = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: formatedTimestamps, // Use formated timestamps for x-axis labels
                    datasets: [
                        {
                            label: '5GHz band Band status',
                            data: bandStatus, // Use band status for y-axis data
                            borderColor: 'rgba(0, 100, 0, 1)', // Dark green border color
                            backgroundColor: 'rgba(0, 100, 0, 0.2)', // Light green background color
                            spanGaps: true,
                            fill: true,
                        },
                    ]
                },
                options: {
                    responsive: true,
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Timestamp'
                            },
                            ticks: {
                                autoSkip: true,
                                maxTicksLimit: 10,
                                minRotation: 45, // Rotate labels by 45 degrees
                                maxRotation: 90 // Maximum rotation
                            },
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Status'
                            },
                            ticks: {
                                autoSkip: false,
                                maxTicksLimit: 2,
                                callback: function(value) {
                                    return value === 1 ? 'ON' : '--'; // Customize tick labels
                                },
                            },
                        }
                    }
                },
            });
            
        },
        processBandStatusData(timestamp, bandStatus) {       
            // Check if timestamp is present in timestamps array
            const idx_in_array = this.band_status.findIndex(element => element.timestamp === timestamp);
            if (idx_in_array !== -1) {
                // append band satus to array
                bandStatus.push(this.band_status[idx_in_array].status);
            } else {
                // if timestamp not present append null
                bandStatus.push(null);
            }
        },
    }
}

</script>

<style scoped>
h2 {
    text-align: center;
}
</style>
