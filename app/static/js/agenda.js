const table = new Tabulator("#schedule-table", {
    data: schedules,
    layout: "fitColumns",
    pagination: true,
    paginationSize: 10,
    columns: [
        { title: "Data", field: "date" },
        { title: "Hora", field: "time" },
        { title: "Paciente", field: "patient" },
        { title: "CPF", field: "cpf" },
        { title: "Médico", field: "doctor" },
        { title: "Especialidade", field: "specialty" },
        { title: "Convênio", field: "insurance" },
        { title: "Status", field: "status" },
    ],
});

const filterField = document.getElementById("filter-field");
const filterValue = document.getElementById("filter-value");


function applyFilter() {
    const field = filterField.value;
    const value = filterValue.value.trim();

    if (!value) {
        table.clearFilter();
        return;
    }

    table.setFilter(field, "like", value);
}

filterField.addEventListener("change", applyFilter);
filterValue.addEventListener("keyup", applyFilter);
