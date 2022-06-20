---
title: Introduction
permalink: /th/Guide/Introduction
---

## Prerequisites <Badge text="Need" type="tip" />

::: tip

- Python ([Basic Python](https://www.w3schools.com/python/))
- HTML ([Basic HTML](https://www.w3schools.com/html/))
- CSS ([Basic CSS](https://www.w3schools.com/css/))
- Javascript ([Basic Javascript](https://www.w3schools.com/js/))
- Electron Framework ([Electron Documents](https://www.electronjs.org/docs/latest))
- Vue Framework ([Vue js Docs](https://vuejs.org/guide/introduction.html))
- Protocol HTTP([Protocol Layer](https://www.cloudflare.com/en-ca/learning/network-layer/what-is-a-protocol/))
- API ([What is API](https://www.mulesoft.com/resources/api/what-is-an-api))
- JSON([JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) , [JSON with Python](https://stackpython.co/tutorial/json-python))
- Asynchronous ([Asynchronous Programming in Python](https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb))
- Speech recognition ([Speech recognition](https://realpython.com/python-speech-recognition/))
- Environments Python ([Virtual Environments Python](https://docs.python.org/3/library/venv.html))
- Wit AI ([Wit.ai Documents](https://wit.ai/docs))
- OpenWeather ([OpenWeatherMap](https://openweathermap.org/api))
- Google Knowledge Graph ([Google Knowledge Graph Docs](https://developers.google.com/knowledge-graph))
  :::

## Mini Workflow Backend

```flow
st=>start: Start
input_talk=>inputoutput: Talk with AI
send_talkToBackend=>operation: Backend Process Python Flask
intent=>condition: Check Intent in Feature with AI
do_Feature=>subroutine: Feature
out_off_scope=>subroutine: Out of Scope
http=>operation: http request Data from API
api=>inputoutput: API
speech=>inputoutput: AI Talk To User
socket=>operation: Websocket
end=>end: End Process backend

st(bottom)->input_talk
input_talk(right)->send_talkToBackend(bottom)->intent

intent(yes)->do_Feature->http->api->speech
intent(no,bottom)->out_off_scope->speech
speech->socket->end
```

## Mini Workflow Frontend
