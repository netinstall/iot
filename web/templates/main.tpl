<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
  <link rel="stylesheet" href="/static/toggle_checkbox.css">
  <link rel="stylesheet" href="/static/main.css">
  <link rel="yandex-tableau-widget" href="/static/manifest.json" />
  <link rel="icon" type="image/png" href="https://image.flaticon.com/icons/png/512/1185/1185915.png" />
  
  <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
  <script type="text/javascript" src="/static/iot.js"></script>
</head>
<body>

<div class="rounded-lg switch-line">
    <div class="custom-control custom-switch d-inline-block">
      <label class="switch" style="margin-left:-20px;">
      <input onChange="powerControl('star', this.checked)" type="checkbox"  id="customSwitch1" {{devices["star"].state_html()}}>
      <span class="slider round"></span>
    </div>
    <div class="switch-line-right" style="font-size: 16pt;">
      {{devices["star"].name}}
    </div>
</div>

<div class="rounded-lg switch-line">
    <div class="custom-control custom-switch d-inline-block">
      <label class="switch" style="margin-left:-20px;">
      <input onChange="powerControl('tv', this.checked)" type="checkbox"  id="customSwitch1" {{devices["tv"].state_html()}}>
      <span class="slider round"></span>
    </div>
    <div class="switch-line-right" style="font-size: 16pt;">
      <img src="/static/img/tv.png" style="width: 60px">  
    </div>
</div>

<div class="rounded-lg switch-line">
    <div class="custom-control custom-switch d-inline-block">
      <label class="switch" style="margin-left:-20px;">
      <input onChange="powerControl('london', this.checked)" type="checkbox"  id="customSwitch1" {{devices["london"].state_html()}}>
      <span class="slider round"></span>
    </div>
  <div class="switch-line-right">
    <img onClick="selectTvSource('pc')" src="/static/img/pc.png" style="height: 50px">
  </div>
</div>

<div class="rounded-lg switch-line">
  <div class="custom-control custom-switch d-inline-block text-center" style="width: 50%;">
    <img onClick="selectTvSource('youtube')" src="/static/img/youtube.png" style="width:  100px">
  </div>
  <div class="d-inline-block text-center" style="float: right; width: 50%;">
    <img onClick="selectTvSource('netflix')" src="/static/img/netflix.png" style="width: 120px; margin-top: -10px">
  </div>
</div>

<div class="rounded-lg switch-line" style="height:100px">
    <div class="custom-control custom-switch d-inline-block">
      <label class="switch" style="margin-left:-20px; margin-top:15px">
      <input onChange="powerControl('thermostat', this.checked)" type="checkbox"  id="customSwitch1" {{devices["thermostat"].state_html()}}>
      <span class="slider round"></span>
      </label>
    </div>
    <div class="switch-line-right" style="font-size: 16pt;">
      <img src="/static/img/termostat.png" style="width:100px; margin-top:5px;">
      <div style="margin-top:10px; margin-left:7px" class="row">
        <div onClick="temperatureControl(-1)"><img src="/static/img/minus.png" style="height:25px;"></div>
        <div style="font-size:10pt; color:#ccc;  height:25px;border:1px solid; border-color:#ccc; text-align:center">
        	<input id="temperature" value={{devices["thermostat"].temperature()}} class="temperature-input" readonly="readonly"><sup>c°</sup>
        </div>
        <div onClick="temperatureControl(1)"><img src="/static/img/plus.png" style="height:25px;"></div>
      </div>

    </div>
</div>

</body>
</html>
