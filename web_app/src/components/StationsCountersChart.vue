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
        stations_counters: { 
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
        console.log("in mounted StationsCountersChart Vue");
        this.updateChart();
    },
    watch: {
        stations_counters(newValue, oldValue) {
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
            console.log(`Updating stations counters Chart`);
            const ctx = chartRef.value.getContext('2d');

            // Format timestamps 
            const formatedTimestamps = this.timestamps.map(date => date.substring(11, 22));

            // initialize stations counters
            const stationsCounters = this.initializeStationsCounters();

            // Fill stations counters
            this.populateStationsCounters(stationsCounters);

            // Update datasets
            const datasets = this.createDatasets(stationsCounters);

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
                                    text: 'Station counters'
                                }
                            }
                        }
                    },
                });
            }
        },
        initializeStationsCounters() {
            // Extract stations in counters
            const stations = Object.keys(this.stations_counters);
            const stationsCounters = {};
            // Create counters
            for (const station of stations) {
                stationsCounters[station] = {
                txBytes: [],
                rxBytes: [],
                uplinkMCS: [],
                lastDataUplinkRate: [],
                lastDataDownlinkRate: [],
                signalStrength: [],
                avgSignalStrengthByChain: [],
                uplinkShortGuard: [],
                downlinkMCS: [],
                inactive: [],
                signalNoiseRatio: [],
                rxPacketCount: [],
                txPacketCount: [],
                txErrors: [],
                band: [],
                };
            }
            return stationsCounters;
        },
        populateStationsCounters(stationsCounters) {
            // Extract stations in counters
            const stations = Object.keys(this.stations_counters);
            // loop over timestamps array
            this.timestamps.forEach((timestamp) => {
                // loop over stations
                for (const station of stations) {
                    // check if timestamp is present in station counters array
                    const idx = this.stations_counters[station].findIndex(element => element.timestamp === timestamp);
                    if (idx !== -1) {
                        // Append data to station counter
                        this.fillStationData(station, stationsCounters, idx);
                    } else {
                        // Append null values to station counter
                        this.fillStationDataWithNulls(station, stationsCounters);
                    }
                }
            });
        },
        fillStationData(station, stationsCounters, idx) {
            // Extract data
            const data = this.stations_counters[station][idx];
            // Append data to counters
            stationsCounters[station].txBytes.push(data.txBytes);
            stationsCounters[station].rxBytes.push(data.rxBytes);
            stationsCounters[station].uplinkMCS.push(data.uplinkMCS);
            stationsCounters[station].lastDataUplinkRate.push(data.lastDataUplinkRate);
            stationsCounters[station].lastDataDownlinkRate.push(data.lastDataDownlinkRate);
            stationsCounters[station].signalStrength.push(data.signalStrength);
            stationsCounters[station].avgSignalStrengthByChain.push(data.avgSignalStrengthByChain);
            stationsCounters[station].uplinkShortGuard.push(data.uplinkShortGuard);
            stationsCounters[station].downlinkMCS.push(data.downlinkMCS);
            stationsCounters[station].inactive.push(data.inactive);
            stationsCounters[station].signalNoiseRatio.push(data.signalNoiseRatio);
            stationsCounters[station].rxPacketCount.push(data.rxPacketCount);
            stationsCounters[station].txPacketCount.push(data.txPacketCount);
            stationsCounters[station].txErrors.push(data.txErrors);
            stationsCounters[station].band.push(data.band === "2.4GHz" ? 2.4 : 5);
        },
        fillStationDataWithNulls(station, stationsCounters) {
            // Loop over station counter keys
            for (const key of Object.keys(stationsCounters[station])) {
                // Append null to counter
                stationsCounters[station][key].push(null);
            }
        },
        createDatasets(stationsCounters) {
            const datasets = [];
            // Loop over sations
            for (const [index, station] of Object.keys(stationsCounters).entries()) {
                // Get station color
                const { borderColor, backgroundColor } = this.stations_colors[index];
                // Loop over station counters keys
                for (const key of Object.keys(stationsCounters[station])) {
                    // Create dataset
                    datasets.push({
                        label: `${key} ${station}`,
                        data: stationsCounters[station][key],
                        borderColor: borderColor,
                        backgroundColor: backgroundColor,
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
