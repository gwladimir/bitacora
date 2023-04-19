$(document).ready(function () {
  $('#data').DataTable({
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    ajax: {
      url: window.location.pathname,
      type: 'POST',
      dataType: "json",
      data: { 'action': 'searchdata' },
      dataSrc: ""
    },
    columns: [
      // { "data": "id" },
      { "data": "nombre" },
      { "data": "apellido" },
      { "data": "identificacion" },
      { "data": "fecha_registro" },
      { "data": "edad" },
      { "data": "estado" },
      { "data": "opciones" },
    ],
    columnDefs: [
      {
        targets: [-1],
        class: 'text-center',
        orderable: false,
        render: function (data, type, row) {
          var buttons = '<a href="../edit/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
          buttons += '<a href="../delete/' + row.id + '/"  class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
          return buttons;
        }
      },
    ],
    initComplete: function (settings, json) {
    }
  });

});
