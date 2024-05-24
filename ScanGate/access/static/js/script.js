document.addEventListener("DOMContentLoaded", () => {
	const $btnEscanear = document.querySelector("#btnEscanear"),
	$input = document.querySelector("#codigo");
	$btnEscanear.addEventListener("click", ()=>{
		window.open("procesado");
	});

	window.onCodigoLeido = datosCodigo => {
		console.log("Oh sí, código leído: ")
		console.log(datosCodigo)
		$input.value = datosCodigo.codeResult.code;
	}
});