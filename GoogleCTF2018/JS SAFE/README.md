### JS SAFE
[Challenge Link](https://capturetheflag.withgoogle.com/?#beginners/web-js-safe-1)

#### open_safe() function

		<script>
		async function open_safe() {
			keyhole.disabled = true;
  			password = /^CTF{([0-9a-zA-Z_@!?-]+)}$/.exec(keyhole.value);
  			if (!password || !(await x(password[1]))) return document.body.className = 'denied';
  			document.body.className = 'granted';
  			const pwHash = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(password[1])); 
  			const key = await crypto.subtle.importKey('raw', pwHash, alg, false, ['decrypt']);
  			content.value = new TextDecoder("utf-8").decode(await crypto.subtle.decrypt(alg, key, secret))
		}


`password = /^CTF{([0-9a-zA-Z_@!?-]+)}$/.exec(keyhole.value);`

- password[1]: xxxx in CTF{xxxx}
- password[1] will be an argument for function x

#### x(password) function

		async function x(password) {
    		// TODO: check if they can just use Google to get the password once they understand how this works.
		    var code = 'icffjcifkciilckfmckincmfockkpcofqcoircqfscoktcsfucsivcufwcooxcwfycwiAcyfBcwkCcBfDcBiEcDfFcwoGcFfHcFiIcHfJcFkKcJfLcJiMcLfNcwwOcNNPcOOQcPORcQNScRkTcSiUcONVcUoWcOwXcWkYcVkЀcYiЁcЀfЂcQoЃcЂkЄcЃfЅcPNІcЅwЇcІoЈcЇiЉcЈfЊcPkЋcЊiЌcІiЍcЌfЎcWoЏcЎkАcЏiБcІkВcБfГcNkДcГfЕcЇkЖcЕiЗcЖfИcRwЙcИoКcЙkЛcUkМcЛiНcМfОcИkПcОiРcПfСcUwТcСiУcQkФcУiХcЃiЦcQwЧcЦoШcЧkЩcШiЪcЩfЫcRiЬcЫfЭcКiЮcЭfЯcСoаcЯiбcГiвcЙiгcRoдcгkеcдiжdТaзcЛfиdзaжcжийcСkкdйaжcжклcйfмdлaжcжмнdТaжcжноdЀaжcжопdNaжcжпрcUiсcрfтdсaуdЁaтcтутcтофcТfхdфaтcтхтcтктcтнтcтмцdсaтcтцтcтктcтутcтнчaaтшdЯaщcйiъcщfыdъaьcжыэcVfюdэaьcьюьcьояdЛaьcьяьcьуьcьыѐчшьёѐшшђcOfѓdђaѓcѓнѓcѓнєcUfѕdєaѓcѓѕіcЯfїdіaѓcѓїјaёѓљaaтњcжшћcЎiќcћfѝdќaњcњѝњcњeўcЏfџdўaњcњџѠdАaњcњѠњcњшњcњѝњcњfњcњџѡљшњѢaaтѣcжшѣcѣѝѣcѣeѣcѣџѤcЯkѥdѤaѣcѣѥѣcѣшѣcѣѝѣcѣfѣcѣџѦѢшѣѧcцнѧcѧїѨdСaѧcѧѨѧcѧкѧcѧуѩaёѧѪcхмѫdрaѪcѪѫѪcѪкѬdYaѪcѪѬѪcѪиѭaѩѪѮcяюѯdНaѮcѮѯѮcѮиѮcѮхѮcѮкѰaѭѮѱdVaѲcхѱѲcѲѕѳcNoѴcѳkѵcѴfѶdѵaѲcѲѶѲcѲiѲcѲlѲcѲmѷјѲgѸјѭѷѹbѰѸѺcXfѻdѺaѻcѻюѻcѻоѻcѻкѻcѻoѼdђaѻcѻѼѻcѻнѻcѻнѻcѻѕѻcѻїѽaёѻѾѽѹшѿceeҀceeҁcee҂ceeѿaѾeҀјѿT҂ѡҀшҁјh҂hѦҁшѿaѾfҀјѿV҂ѡҀшҁјh҂hѦҁшѿaѾiҀјѿU҂ѡҀшҁјh҂hѦҁшѿaѾjҀјѿX҂ѡҀшҁјh҂hѦҁшѿaѾkҀјѿЁ҂ѡҀшҁјh҂hѦҁшѿaѾlҀјѿF҂ѡҀшҁјh҂hѦҁшѿaѾmҀјѿЄ҂ѡҀшҁјh҂hѦҁшѿaѾnҀјѿЉ҂ѡҀшҁјh҂hѦҁшѿaѾoҀјѿЄ҂ѡҀшҁјh҂hѦҁшѿaѾpҀјѿЋ҂ѡҀшҁјh҂hѦҁшѿaѾqҀјѿЍ҂ѡҀшҁјh҂hѦҁшѿaѾrҀјѿА҂ѡҀшҁјh҂hѦҁшѿaѾsҀјѿF҂ѡҀшҁјh҂hѦҁшѿaѾtҀјѿВ҂ѡҀшҁјh҂hѦҁшѿaѾuҀјѿД҂ѡҀшҁјh҂hѦҁшѿaѾvҀјѿЗ҂ѡҀшҁјh҂hѦҁшѿaѾwҀјѿК҂ѡҀшҁјh҂hѦҁшѿaѾxҀјѿН҂ѡҀшҁјh҂hѦҁшѿaѾyҀјѿР҂ѡҀшҁјh҂hѦҁшѿaѾAҀјѿТ҂ѡҀшҁјh҂hѦҁшѿaѾBҀјѿФ҂ѡҀшҁјh҂hѦҁшѿaѾCҀјѿW҂ѡҀшҁјh҂hѦҁшѿaѾDҀјѿХ҂ѡҀшҁјh҂hѦҁшѿaѾEҀјѿЪ҂ѡҀшҁјh҂hѦҁшѿaѾFҀјѿЬ҂ѡҀшҁјh҂hѦҁшѿaѾGҀјѿЮ҂ѡҀшҁјh҂hѦҁшѿaѾHҀјѿа҂ѡҀшҁјh҂hѦҁшѿaѾIҀјѿe҂ѡҀшҁјh҂hѦҁшѿaѾJҀјѿб҂ѡҀшҁјh҂hѦҁшѿaѾKҀјѿв҂ѡҀшҁјh҂hѦҁшѿaѾLҀјѿK҂ѡҀшҁјh҂hѦҁшѿaѾMҀјѿе҂ѡҀшҁјh҂hѦҁшѐceeёceeѓceeјceeљceeњceeѡceeѢceeѣceeѦceeѧceeѩceeѪceeѭceeѮceeѰceeѲceeѷceeѸceeѹceeѻceeѽceeѾceeҀceeҁceeжceeтceeчceeьcee'
		    var env = {
		        a: (x,y) => x[y],
		        b: (x,y) => Function.constructor.apply.apply(x, y),
		        c: (x,y) => x+y,
		        d: (x) => String.fromCharCode(x),
		        e: 0,
		        f: 1,
		        g: new TextEncoder().encode(password),
		        h: 0,
		    };
		    for (var i = 0; i < code.length; i += 4) {
		        var [lhs, fn, arg1, arg2] = code.substr(i, 4);
		        try {
		            env[lhs] = env[fn](env[arg1], env[arg2]);
		        } catch(e) {
		            env[lhs] = new env[fn](env[arg1], env[arg2]);
		        }
		        if (env[lhs] instanceof Promise) env[lhs] = await env[lhs];
		    }
		    return !env.h;
		}

`g: new TextEncoder().encode(password)`

- we know env[g] will parse password
- we first need to check when variable lhs, fn, arg1 or arg2 becomes g

#### Inject debugging javascript

		...
		var [lhs, fn, arg1, arg2] = code.substr(i, 4);
		var chars = [lhs, fn, arg1, arg2]; //added for debugging
		...
		if (env[lhs] instanceof Promise) env[lhs] = await env[lhs];
		//Debugging Code Here
		...
		}
		return !env.h;

- Debugging 01
	- As mentioned above, I thought `env[g]` is the key and tried to find when the one of `[lhs, fn, arg1, arg2]` will be `g` 
	- I used `1111` for password and found `i == 876` (This number will change as the length of password changes)
- 

		...
		var [lhs, fn, arg1, arg2] = code.substr(i, 4);
		var chars = [lhs, fn, arg1, arg2]; //added for debugging
		...
		if (env[lhs] instanceof Promise) env[lhs] = await env[lhs];
		//Debugging Code Here
		...
		}
		return !env.h;
		
		...
		var [lhs, fn, arg1, arg2] = code.substr(i, 4);
		var chars = [lhs, fn, arg1, arg2];
		try {
		...
		if (env[lhs] instanceof Promise) env[lhs] = await env[lhs];
		if (chars.includes("g")) {
			console.log('----------');
			console.log('i:',i);
			console.log('lhs:',lhs);
			console.log('fn:',fn);
			console.log('arg1:',arg1);
			console.log('arg2:',arg2);
			console.log('env[lhs]:',env[lhs]);
			console.log('env[fn]:',env[fn]);
			console.log('env[arg1]:',env[arg1]);
			console.log('env[arg2]:',env[arg2]);
			console.log('env:',env);
			console.log('----------');		
			break;
		}
		}

		
- Debugging 02
	- I wanted to know when `env[h]` will be affected after `env[g]` is hit and found `i == 976` 
- 

		...
		var [lhs, fn, arg1, arg2] = code.substr(i, 4);
		var chars = [lhs, fn, arg1, arg2]; 
		...
		if (env[lhs] instanceof Promise) env[lhs] = await env[lhs];
		if (i >= 876 && lhs == "h") { // changing conditions
			... //same as above
		}
		}

	- I also found something interesting while going through `env` array
		- `Ѿ: Uint8Array(32) [15, 254, 26, 189, 26, 8, 33, 83, 83, 194, 51, 214, 224, 9, 97, 62, 149, 238, 196, 37, 56, 50, 167, 97, 175, 40, 255, 55, 172, 90, 21, 12]`
	- Futher analysis reveals it is `sha256` hash of the password, `1111` (Google Search)
-	 	
	
		>>> l = [15, 254, 26, 189, 26, 8, 33, 83, 83, 194, 51, 214, 224, 9, 97, 62, 149, 238, 196, 37, 56, 50, 167, 97, 175, 40, 255, 55, 172, 90, 21, 12]
		>>> m=''
		>>> for _ in l:
		...     m += hex(_)[2:].zfill(2)
		...
		>>> m
		'0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'

	`$ echo -n '1111' | shasum -t -a 256`
	`0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c`		
- Debugging 03 
	- So, from here I went through the loop from when `i == 976` to `i == 1024`, just a random pick.
- 

		...
		var [lhs, fn, arg1, arg2] = code.substr(i, 4);
		var chars = [lhs, fn, arg1, arg2]; 
		...
		if (env[lhs] instanceof Promise) env[lhs] = await env[lhs];
		if (i >= 976 && i <= 1024) {
			...
			//break;
		}
		}

	- And found some interesting arrays
		- `env[lhs]: (2) [254, 104]`
		- `env[lhs]: (2) [26, 96]`
		- `env[lhs]: (2) [189, 84]`
	- When lhs is `Ҁ`, it seemed the script is paring the characters from `sha256` array in "Debugging 2" with some other characters 
	
- Debugging 04
	- So I collected all the coressponding characters in an array, `my_arry` 
	- Since the starting chracter I got in the previous step is the second character from `sha256` array, I lowered the starting number to 964 after manual analysis. 
- 

		var my_arry = []; // before loop to get result
		...
		var [lhs, fn, arg1, arg2] = code.substr(i, 4);
		var chars = [lhs, fn, arg1, arg2]; 
		...
		if (env[lhs] instanceof Promise) env[lhs] = await env[lhs];
		if (i >= 964 && lhs == "Ҁ") {
			my_arry.push(env[lhs][1]) // result array
			//break;
		}
		}
		console.log(my_arry); //print result array
		return !env.h;

	- I got below array and extract the hash
		- `(33) [230, 104, 96, 84, 111, 24, 205, 187, 205, 134, 179, 94, 24, 181, 37, 191, 252, 103, 247, 114, 198, 80, 206, 223, 227, 255, 122, 0, 38, 250, 29, 238, undefined]`
- 

		>>> my_arry = [230, 104, 96, 84, 111, 24, 205, 187, 205, 134, 179, 94, 24, 181, 37, 191, 252, 103, 247, 114, 198, 80, 206, 223, 227, 255, 122, 0, 38, 250, 29, 238]`
		>>> hash=''
		>>> for _ in my_arry:
		...     hash += hex(_)[2:].zfill(2)
		...
		>>> hash
		'e66860546f18cdbbcd86b35e18b525bffc67f772c650cedfe3ff7a0026fa1dee'
		
	- Google search revealed the hash is for `Passw0rd!`
	
	`$ echo -n 'Passw0rd!' | shasum -t -a 256`
	`e66860546f18cdbbcd86b35e18b525bffc67f772c650cedfe3ff7a0026fa1dee`