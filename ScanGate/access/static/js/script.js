window.addEventListener('load', function () {
    let selectedDeviceId;
    const codeReader = new ZXing.BrowserMultiFormatReader()
    console.log('El lector de código esta iniciado')

    codeReader.listVideoInputDevices()

        .then((videoInputDevices) => {

            if (videoInputDevices.length >= 2 ) {
              selectedDeviceId = videoInputDevices[1].deviceId
            }
            else {
                selectedDeviceId = videoInputDevices[0].deviceId
            }

            document.getElementById('startButton').addEventListener('click', () => {
                codeReader.decodeFromVideoDevice(selectedDeviceId, 'video', (result, err) => {
                    if (result) {
                        console.log(result)
                        // Redirigir a /perfil/ seguido del resultado del código de barras
                        window.location.href = `/perfil/${result.text}`;
                    }
                    if (err && !(err instanceof ZXing.NotFoundException)) {
                        console.error(err)
                        document.getElementById('result').textContent = err
                    }
                })
                
            })
        })
        .catch((err) => {
            console.error(err)
        })
})