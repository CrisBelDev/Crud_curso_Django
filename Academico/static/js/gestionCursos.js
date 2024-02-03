(function(){
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion = confirm('Seguro de eliminar este curso?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });

    // Cerrar la alerta después de 5 segundos
    setTimeout(function() {
        var alerta = document.getElementById('alerta');
        var bsAlert = new bootstrap.Alert(alerta);
        bsAlert.close();
    }, 5000);
})();
