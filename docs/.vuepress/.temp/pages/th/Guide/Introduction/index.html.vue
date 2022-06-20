<template><div><h2 id="prerequisites" tabindex="-1"><a class="header-anchor" href="#prerequisites" aria-hidden="true">#</a> Prerequisites <Badge text="Need" type="tip" /></h2>
<div class="custom-container tip"><p class="custom-container-title">Tips</p>
<ul>
<li>Python (<a href="https://www.w3schools.com/python/" target="_blank" rel="noopener noreferrer">Basic Python<ExternalLinkIcon/></a>)</li>
<li>HTML (<a href="https://www.w3schools.com/html/" target="_blank" rel="noopener noreferrer">Basic HTML<ExternalLinkIcon/></a>)</li>
<li>CSS (<a href="https://www.w3schools.com/css/" target="_blank" rel="noopener noreferrer">Basic CSS<ExternalLinkIcon/></a>)</li>
<li>Javascript (<a href="https://www.w3schools.com/js/" target="_blank" rel="noopener noreferrer">Basic Javascript<ExternalLinkIcon/></a>)</li>
<li>Electron Framework (<a href="https://www.electronjs.org/docs/latest" target="_blank" rel="noopener noreferrer">Electron Documents<ExternalLinkIcon/></a>)</li>
<li>Vue Framework (<a href="https://vuejs.org/guide/introduction.html" target="_blank" rel="noopener noreferrer">Vue js Docs<ExternalLinkIcon/></a>)</li>
<li>Protocol HTTP(<a href="https://www.cloudflare.com/en-ca/learning/network-layer/what-is-a-protocol/" target="_blank" rel="noopener noreferrer">Protocol Layer<ExternalLinkIcon/></a>)</li>
<li>API (<a href="https://www.mulesoft.com/resources/api/what-is-an-api" target="_blank" rel="noopener noreferrer">What is API<ExternalLinkIcon/></a>)</li>
<li>JSON(<a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON" target="_blank" rel="noopener noreferrer">JSON<ExternalLinkIcon/></a> , <a href="https://stackpython.co/tutorial/json-python" target="_blank" rel="noopener noreferrer">JSON with Python<ExternalLinkIcon/></a>)</li>
<li>Asynchronous (<a href="https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb" target="_blank" rel="noopener noreferrer">Asynchronous Programming in Python<ExternalLinkIcon/></a>)</li>
<li>Speech recognition (<a href="https://realpython.com/python-speech-recognition/" target="_blank" rel="noopener noreferrer">Speech recognition<ExternalLinkIcon/></a>)</li>
<li>Environments Python (<a href="https://docs.python.org/3/library/venv.html" target="_blank" rel="noopener noreferrer">Virtual Environments Python<ExternalLinkIcon/></a>)</li>
<li>Wit AI (<a href="https://wit.ai/docs" target="_blank" rel="noopener noreferrer">Wit.ai Documents<ExternalLinkIcon/></a>)</li>
<li>OpenWeather (<a href="https://openweathermap.org/api" target="_blank" rel="noopener noreferrer">OpenWeatherMap<ExternalLinkIcon/></a>)</li>
<li>Google Knowledge Graph (<a href="https://developers.google.com/knowledge-graph" target="_blank" rel="noopener noreferrer">Google Knowledge Graph Docs<ExternalLinkIcon/></a>)</li>
</ul>
</div>
<h2 id="mini-workflow-backend" tabindex="-1"><a class="header-anchor" href="#mini-workflow-backend" aria-hidden="true">#</a> Mini Workflow Backend</h2>
<FlowChart id="flowchart-382ee223" code="st%3D%3Estart%3A%20Start%0Ainput_talk%3D%3Einputoutput%3A%20Talk%20with%20AI%0Asend_talkToBackend%3D%3Eoperation%3A%20Backend%20Process%20Python%20Flask%0Aintent%3D%3Econdition%3A%20Check%20Intent%20in%20Feature%20with%20AI%0Ado_Feature%3D%3Esubroutine%3A%20Feature%0Aout_off_scope%3D%3Esubroutine%3A%20Out%20of%20Scope%0Ahttp%3D%3Eoperation%3A%20http%20request%20Data%20from%20API%0Aapi%3D%3Einputoutput%3A%20API%0Aspeech%3D%3Einputoutput%3A%20AI%20Talk%20To%20User%0Asocket%3D%3Eoperation%3A%20Websocket%0Aend%3D%3Eend%3A%20End%20Process%20backend%0A%0Ast(bottom)-%3Einput_talk%0Ainput_talk(right)-%3Esend_talkToBackend(bottom)-%3Eintent%0A%0Aintent(yes)-%3Edo_Feature-%3Ehttp-%3Eapi-%3Espeech%0Aintent(no%2Cbottom)-%3Eout_off_scope-%3Espeech%0Aspeech-%3Esocket-%3Eend%0A" preset="vue"></FlowChart><h2 id="mini-workflow-frontend" tabindex="-1"><a class="header-anchor" href="#mini-workflow-frontend" aria-hidden="true">#</a> Mini Workflow Frontend</h2>
</div></template>
