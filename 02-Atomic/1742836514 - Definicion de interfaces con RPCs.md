---
aliases:
  - Definicion de interfaces con RPCs
tags:
References:
cssclasses:
---
# Definicion de interfaces con RPCs
```RPC
program programName {
	version programVersion{
		int serviceName(params) = opNum;
		int serviceName(params) = opNum;
		...
		} = versionNum;
	} = programNum;
```

> **PRÁCTICA:** Usar el NIA como número de programa para que, si usando guernika, no haya conflictos 
***