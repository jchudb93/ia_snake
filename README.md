# IA snake


## Requerimientos

El código ha sido escrito en Python 3.6. 

Para instalar las dependencias:
```
$ make deps
```

## Entrenar el agente con DQN
Para entrenar el agente con la configuración por fecto:
```
$ make train
```

El modelo del agente será guardado con el nombre  `dqn-final.model`.

Ejecutar `train.py` para cambiar el nivel y el número de episodios (revisar `train.py -h`).

## Juego

El comportamiento del agente puede ser probado en CLI y revisar diferentes estadísticas o verse en GUI para ver cada acción ejecutada.

Para probar el agente con CLI, ejecutar el siguiente comando y revisar el archivo **.csv** generado:
```
$ make play
```

Para ejecutar solo con GUI:
```
$ make play-gui
```

Para ejecutar el juego con GUI y teclado:
```
$ make play-human
```

## Ejecutar pruebas
```
$ make test
```

Basado en:
https://github.com/YuriyGuts/snake-ai-reinforcement