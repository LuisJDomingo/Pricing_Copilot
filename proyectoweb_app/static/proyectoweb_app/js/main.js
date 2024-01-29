const getOptionChart = async () => {
    try {
        const response = await fetch("/proveedores/grafico_inventario/");
        if (response.ok) {
            return await response.json();
        } else {
            console.error("Error en la respuesta del servidor");
        }
    } catch (error) {
        console.error("Error al obtener los datos del gráfico:", error);
    }
    return {};
};

const initChart = async () => {
    const myChart = echarts.init(document.getElementById("chart"));
    const option = await getOptionChart();
    myChart.setOption(option);
    myChart.resize();
};

window.addEventListener("load", async () => {
    await initChart();
});

