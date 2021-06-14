function powerControl(device, action) {
    $.post('/action/power_control', {
        action: action,
        device: device
    }, );
}

function selectTvSource(source) {
    $.post('/action/tv/source', {
        source: source
    }, );
}

function temperatureControl(temp_diff) {
    currentTemp = +document.getElementById("temperature").value
    newTemp = currentTemp + temp_diff
    $.post('/action/temperature_control', {
        temperature: newTemp
    }, );
    document.getElementById("temperature").value = newTemp
}
