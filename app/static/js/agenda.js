new Tabulator("#schedule-table", {
    data: schedules,

    layout: "fitColumns",

    pagination: true,
    paginationSize: 10,

    columns: [
        {
            title: "Paciente",
            field: "patient"
        },
        {
            title: "CPF",
            field: "cpf"
        },
        {
            title: "Médico",
            field: "doctor"
        },
        {
            title: "Especialidade",
            field: "specialty"
        },
        {
            title: "Data",
            field: "date"
        },
        {
            title: "Hora",
            field: "time"
        }
    ]
});