function statusFormatter(cell) {
    const status = String(cell.getValue() || "").trim();
    const normalized = status.toLowerCase();

    const typeByStatus = {
        agendado: "agendado",
        cancelado: "cancelado",
        reagendado: "reagendado",
    };

    const className = typeByStatus[normalized] || "default";
    return `<span class="status-pill status-pill-${className}">${status || "Sem status"}</span>`;
}

const table = new Tabulator("#schedule-table", {
    data: schedules,
    layout: "fitColumns",
    pagination: true,
    paginationSize: 10,
    responsiveLayout: "collapse",
    placeholder: "Nenhum agendamento encontrado para os filtros atuais.",
    columns: [
        {
            title: "Data",
            field: "date",
            sorter: "date",
            formatter(cell) {
                const [year, month, day] = cell.getValue().split("-");

                return `${day}/${month}/${year}`;
            },
        },
        { title: "Hora", field: "time" },
        { title: "Paciente", field: "patient" },
        { title: "CPF", field: "cpf" },
        { title: "Médico", field: "doctor" },
        { title: "Especialidade", field: "specialty" },
        { title: "Convênio", field: "insurance" },
        { title: "Status", field: "status", formatter: statusFormatter, hozAlign: "center" },
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
