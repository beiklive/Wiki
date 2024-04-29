---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==

# Text Elements
假设内存大小
为40字节 ^7wltgCvi

10 bytes ^22pp5hWR

10 bytes ^nnoNAFMf

释放 10 bytes ^HgQSt1Oc

释放 10 bytes ^looNn2Hw

现在需要申请 15 字节
剩余内存有 20 字节，
内存空间虽然足够，但是
因为不连续导致申请失败
 ^ir8rcOMx

8  16  24  32  40  48  56  64  72  80  88  96  104  112  120  128 ^3FOwUTpB

0  1   2   3   4   5   6   7   8   9  10  11  12    13   14   15    数组下标 ^JCGuNedH

对应的字节数 ^Fhm7o26I

所需字节数 ^3hnwUTUd

大于128字节？ ^yWYJdqib

由一级空间配置器申请 ^7E4wgkDR

是 ^FF0BCCvl

选择要使用的桶 ^VckFwQxf

否 ^0audJkQa

该桶下是否已挂上内存块 ^3iEsfAzp

将桶上第一个小块
内存返回给用户 ^oy8ZfBAC

是 ^TkScQM6P

否 ^8jBNNBdC

向桶中填充小块内存 ^s6X9W0N2

计算 num 个 n 字节大小的内存块所需的大小以及内存池的剩余空间 ^EdE4Bttr

能否提供 num 块 ^D6NKNDmz

能否提供 至少 1 块 ^1e8yJMaw

切割并返回空间 ^UNNAlAPQ

是 ^ESW5bqim

是 ^Qac63gLA

否 ^A119Ajtr

内存池空间不足，最小的 n    大小的内存块都不能提供。
将内存池中剩余内存挂接到桶中 ^jCyiP4tp

否 ^ZN5dJHNv

通过系统堆向内存池中补充内存 ^9zXHAx01

补充成功 ^i6Z7FOT6

是 ^I2nxtDD7

从哈希桶中大块的桶中取出内存块补充 ^kHlwu3ga

否 ^KvVPwkwG

补充成功 ^rjfDGJtN

向一级空间配置器申请补充 ^V9bbn86i

否 ^CbWWZ13I

是 ^GIUbYFlH

只填充了一块？ ^jwdTwWwB

直接将该块内存返回给用户 ^TKfsLjop

将第一块内存返回给用户，剩余内存挂入桶中 ^m3lF7tWD

是 ^0US48Ksk

否 ^jaaFqsdf

填充流程 ^GdPBLNmc

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.1.6",
	"elements": [
		{
			"type": "rectangle",
			"version": 92,
			"versionNonce": 1517705716,
			"isDeleted": false,
			"id": "57vYi_hUgZICc95CvsVNT",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1034.2428479875837,
			"y": 336.285699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 1416.2500000000002,
			"height": 57.5,
			"seed": 212683340,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "p-qQBHcpZu5v302CP7G7C",
					"type": "arrow"
				}
			],
			"updated": 1710394051073,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "rectangle",
			"version": 221,
			"versionNonce": 512737268,
			"isDeleted": false,
			"id": "IGhSJhj5P9Ao5boa5rdHn",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 400.8000183105469,
			"y": 290.20001220703125,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffec99",
			"width": 202.39999389648438,
			"height": 275.20001220703125,
			"seed": 728606708,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 57,
			"versionNonce": 591620428,
			"isDeleted": false,
			"id": "gEH4a3Fu9SzdBPGkil9mY",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 404,
			"y": 427,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffec99",
			"width": 193.60003662109375,
			"height": 0.79998779296875,
			"seed": 69898740,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					193.60003662109375,
					-0.79998779296875
				]
			]
		},
		{
			"type": "line",
			"version": 49,
			"versionNonce": 872128884,
			"isDeleted": false,
			"id": "rHS-_sk6sSbwKhsLQYEdc",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 401.6000061035156,
			"y": 355.8000183105469,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffec99",
			"width": 192.80001831054688,
			"height": 3.20001220703125,
			"seed": 1960125940,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					192.80001831054688,
					-3.20001220703125
				]
			]
		},
		{
			"type": "line",
			"version": 50,
			"versionNonce": 1411407820,
			"isDeleted": false,
			"id": "tMsaAnXQVF-hz4MQP8FLI",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 403.20001220703125,
			"y": 499,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffec99",
			"width": 194.4000244140625,
			"height": 8,
			"seed": 116495564,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					194.4000244140625,
					-8
				]
			]
		},
		{
			"type": "line",
			"version": 290,
			"versionNonce": 1148146420,
			"isDeleted": false,
			"id": "aA5aSxlgigwPW-AEkzeWd",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 364.79998779296875,
			"y": 292.6000061035156,
			"strokeColor": "#f08c00",
			"backgroundColor": "#ffec99",
			"width": 4,
			"height": 276.8000183105469,
			"seed": 1505416012,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-4,
					276.8000183105469
				]
			]
		},
		{
			"type": "line",
			"version": 22,
			"versionNonce": 2065335884,
			"isDeleted": false,
			"id": "-q1pkzz75bhWXFmx3kABW",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 362.3999938964844,
			"y": 287,
			"strokeColor": "#f08c00",
			"backgroundColor": "#ffec99",
			"width": 24,
			"height": 0.800018310546875,
			"seed": 870239220,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					24,
					0.800018310546875
				]
			]
		},
		{
			"type": "line",
			"version": 25,
			"versionNonce": 1047581812,
			"isDeleted": false,
			"id": "MkgkPd8IzFOC_bACWcqkJ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 360,
			"y": 568.6000366210938,
			"strokeColor": "#f08c00",
			"backgroundColor": "#ffec99",
			"width": 24.800018310546875,
			"height": 3.20001220703125,
			"seed": 269314932,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					24.800018310546875,
					-3.20001220703125
				]
			]
		},
		{
			"type": "text",
			"version": 188,
			"versionNonce": 1024187596,
			"isDeleted": false,
			"id": "7wltgCvi",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 219.20001220703125,
			"y": 391.0000305175781,
			"strokeColor": "#f08c00",
			"backgroundColor": "#ffec99",
			"width": 113.45993041992188,
			"height": 43.50580651785852,
			"seed": 1745254860,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"fontSize": 18.915568051242836,
			"fontFamily": 2,
			"text": "假设内存大小\n为40字节",
			"rawText": "假设内存大小\n为40字节",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "假设内存大小\n为40字节",
			"lineHeight": 1.15
		},
		{
			"type": "text",
			"version": 34,
			"versionNonce": 1338385908,
			"isDeleted": false,
			"id": "22pp5hWR",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 464,
			"y": 310.1999816894531,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#ffec99",
			"width": 81.81993103027344,
			"height": 25,
			"seed": 1829770188,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "10 bytes",
			"rawText": "10 bytes",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "10 bytes",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 79,
			"versionNonce": 328098636,
			"isDeleted": false,
			"id": "nnoNAFMf",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 460.397216796875,
			"y": 448.1000061035156,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#ffec99",
			"width": 81.81993103027344,
			"height": 25,
			"seed": 1535107572,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "10 bytes",
			"rawText": "10 bytes",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "10 bytes",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 38,
			"versionNonce": 2104838004,
			"isDeleted": false,
			"id": "HgQSt1Oc",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 451.20001220703125,
			"y": 378.1999816894531,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffec99",
			"width": 131.81993103027344,
			"height": 25,
			"seed": 1314865740,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "释放 10 bytes",
			"rawText": "释放 10 bytes",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "释放 10 bytes",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 62,
			"versionNonce": 888936908,
			"isDeleted": false,
			"id": "looNn2Hw",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 440.81890869140625,
			"y": 518.2999267578125,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffec99",
			"width": 131.81993103027344,
			"height": 25,
			"seed": 292024140,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "释放 10 bytes",
			"rawText": "释放 10 bytes",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "释放 10 bytes",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 173,
			"versionNonce": 2087649356,
			"isDeleted": false,
			"id": "ir8rcOMx",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 636,
			"y": 374.9999694824219,
			"strokeColor": "#f08c00",
			"backgroundColor": "#ffec99",
			"width": 220,
			"height": 115,
			"seed": 1480465652,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 2,
			"text": "现在需要申请 15 字节\n剩余内存有 20 字节，\n内存空间虽然足够，但是\n因为不连续导致申请失败\n",
			"rawText": "现在需要申请 15 字节\n剩余内存有 20 字节，\n内存空间虽然足够，但是\n因为不连续导致申请失败\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "现在需要申请 15 字节\n剩余内存有 20 字节，\n内存空间虽然足够，但是\n因为不连续导致申请失败\n",
			"lineHeight": 1.15
		},
		{
			"type": "text",
			"version": 160,
			"versionNonce": 596603596,
			"isDeleted": false,
			"id": "3FOwUTpB",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 1051.7428479875837,
			"y": 342.53569902692504,
			"strokeColor": "#f08c00",
			"backgroundColor": "#ffec99",
			"width": 1371.09375,
			"height": 43.199999999999996,
			"seed": 587629388,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "phzO-I9RtI--AVoE5-vgg",
					"type": "arrow"
				},
				{
					"id": "bYfWJSc4il4xhySVIU7as",
					"type": "arrow"
				},
				{
					"id": "0EBPf3pRnX_Wgj2n2oFoH",
					"type": "arrow"
				},
				{
					"id": "x5gL0yqYXkUqAIgEOIsS8",
					"type": "arrow"
				},
				{
					"id": "4aos56TmvczGt-URyHOe8",
					"type": "arrow"
				}
			],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"fontSize": 36,
			"fontFamily": 3,
			"text": "8  16  24  32  40  48  56  64  72  80  88  96  104  112  120  128",
			"rawText": "8  16  24  32  40  48  56  64  72  80  88  96  104  112  120  128",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "8  16  24  32  40  48  56  64  72  80  88  96  104  112  120  128",
			"lineHeight": 1.2
		},
		{
			"type": "line",
			"version": 29,
			"versionNonce": 896462836,
			"isDeleted": false,
			"id": "hvHYvfQvAM6_to_QfaAuK",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1101.7428479875837,
			"y": 333.785699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 0,
			"height": 61.25,
			"seed": 1525457740,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0,
					61.25
				]
			]
		},
		{
			"type": "line",
			"version": 26,
			"versionNonce": 1362049356,
			"isDeleted": false,
			"id": "rRZBywlJ9VTdhygfdn1eE",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1177.9928479875837,
			"y": 333.785699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 1.25,
			"height": 58.75,
			"seed": 564965364,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-1.25,
					58.75
				]
			]
		},
		{
			"type": "line",
			"version": 29,
			"versionNonce": 125096308,
			"isDeleted": false,
			"id": "2ZBrJoN7z8BoOuKBR3YGD",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1265.4928479875837,
			"y": 333.785699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 2.5,
			"height": 53.75,
			"seed": 1555846476,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-2.5,
					53.75
				]
			]
		},
		{
			"type": "line",
			"version": 22,
			"versionNonce": 1947348940,
			"isDeleted": false,
			"id": "bciVwk4u1dJUJsdLo7QWG",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1345.4928479875837,
			"y": 336.285699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 2.5,
			"height": 62.5,
			"seed": 346938868,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					2.5,
					62.5
				]
			]
		},
		{
			"type": "line",
			"version": 26,
			"versionNonce": 826442484,
			"isDeleted": false,
			"id": "ayehbWXvHZF-p459cOYxk",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1426.7428479875837,
			"y": 338.785699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 5,
			"height": 55,
			"seed": 1583222092,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-5,
					55
				]
			]
		},
		{
			"type": "line",
			"version": 24,
			"versionNonce": 1548899916,
			"isDeleted": false,
			"id": "RTNXRyLC_OxCBctPBB8jl",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1505.4928479875837,
			"y": 338.785699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 0,
			"height": 51.25,
			"seed": 115745140,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0,
					51.25
				]
			]
		},
		{
			"type": "line",
			"version": 19,
			"versionNonce": 157156468,
			"isDeleted": false,
			"id": "OAT_mfgafMEo-MOpHYjpt",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1592.9928479875837,
			"y": 337.535699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 0,
			"height": 53.75,
			"seed": 1999732428,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0,
					53.75
				]
			]
		},
		{
			"type": "line",
			"version": 29,
			"versionNonce": 1187622092,
			"isDeleted": false,
			"id": "sDsamgt3WbFlrg7gxD_0I",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1680.4928479875837,
			"y": 335.035699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 1.25,
			"height": 61.25,
			"seed": 1537187188,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-1.25,
					61.25
				]
			]
		},
		{
			"type": "line",
			"version": 27,
			"versionNonce": 630019572,
			"isDeleted": false,
			"id": "OKG-Y-5KGUvzwXxib9ByL",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1762.9928479875837,
			"y": 337.535699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 2.5,
			"height": 55,
			"seed": 759399244,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					2.5,
					55
				]
			]
		},
		{
			"type": "line",
			"version": 15,
			"versionNonce": 1158820684,
			"isDeleted": false,
			"id": "00mRb9sqCZ-b5gy3NlWX1",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1846.7428479875837,
			"y": 336.285699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 3.75,
			"height": 55,
			"seed": 1297317108,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					3.75,
					55
				]
			]
		},
		{
			"type": "line",
			"version": 20,
			"versionNonce": 1926657908,
			"isDeleted": false,
			"id": "v22Cra0uNKRb_LXd5RuDe",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1932.9928479875837,
			"y": 332.535699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 2.5,
			"height": 61.25,
			"seed": 1110458572,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					2.5,
					61.25
				]
			]
		},
		{
			"type": "line",
			"version": 28,
			"versionNonce": 629533132,
			"isDeleted": false,
			"id": "N2sJ4Piv8NpRZ5fEKpW4q",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2015.4928479875837,
			"y": 335.035699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 2.5,
			"height": 58.75,
			"seed": 486452468,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					2.5,
					58.75
				]
			]
		},
		{
			"type": "line",
			"version": 24,
			"versionNonce": 1300195572,
			"isDeleted": false,
			"id": "RyDMQVQWRgd5ZaPPmFxj-",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2122.992847987584,
			"y": 331.285699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 2.5,
			"height": 63.75,
			"seed": 790562124,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-2.5,
					63.75
				]
			]
		},
		{
			"type": "line",
			"version": 23,
			"versionNonce": 1530843212,
			"isDeleted": false,
			"id": "UaRb8JXiyeHcKpumeN3cg",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2235.492847987584,
			"y": 336.285699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 7.5,
			"height": 57.5,
			"seed": 1153742452,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-7.5,
					57.5
				]
			]
		},
		{
			"type": "line",
			"version": 29,
			"versionNonce": 420358772,
			"isDeleted": false,
			"id": "0DUenpzxr_OnqClW1Vpgw",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2336.742847987584,
			"y": 335.035699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 2.5,
			"height": 61.25,
			"seed": 231916364,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-2.5,
					61.25
				]
			]
		},
		{
			"type": "arrow",
			"version": 490,
			"versionNonce": 709665740,
			"isDeleted": false,
			"id": "phzO-I9RtI--AVoE5-vgg",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1026.4633863291647,
			"y": 436.81234785765713,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 79.21913449656849,
			"height": 1.2249633422672892,
			"seed": 1022261708,
			"groupIds": [
				"1f5vuaP-_ozeWvRlYqhnz"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "3FOwUTpB",
				"focus": 0.9779436920210537,
				"gap": 11.203449389688018
			},
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					79.21913449656849,
					-1.2249633422672892
				]
			]
		},
		{
			"type": "line",
			"version": 475,
			"versionNonce": 1763266292,
			"isDeleted": false,
			"id": "7MoC7xlE9jF1AY0Wf_flo",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1066.3454827326414,
			"y": 471.2612486500786,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.3875181934722878,
			"height": 9.933649782463025,
			"seed": 387276876,
			"groupIds": [
				"1f5vuaP-_ozeWvRlYqhnz"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.3875181934722878,
					9.933649782463025
				]
			]
		},
		{
			"type": "line",
			"version": 460,
			"versionNonce": 1260276300,
			"isDeleted": false,
			"id": "275n3XYm6TiQ9y_frr6Wb",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1064.2367531234709,
			"y": 478.55083921990826,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 10.093050375373764,
			"height": 5.352903824739634,
			"seed": 144406220,
			"groupIds": [
				"1f5vuaP-_ozeWvRlYqhnz"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					10.093050375373764,
					5.352903824739634
				]
			]
		},
		{
			"type": "line",
			"version": 472,
			"versionNonce": 880496756,
			"isDeleted": false,
			"id": "yQEA3HQRkeqadYDqTKfB3",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1068.6463171196665,
			"y": 479.14808541564724,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 9.445342561429221,
			"height": 4.995069092088584,
			"seed": 1041939788,
			"groupIds": [
				"1f5vuaP-_ozeWvRlYqhnz"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-9.445342561429221,
					4.995069092088584
				]
			]
		},
		{
			"type": "arrow",
			"version": 546,
			"versionNonce": 1345528692,
			"isDeleted": false,
			"id": "0EBPf3pRnX_Wgj2n2oFoH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1185.333394017295,
			"y": 436.8201296539034,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 79.21913449656849,
			"height": 1.2249633422672892,
			"seed": 86606324,
			"groupIds": [
				"WZwFAMKZadmBjAFpYFy_C"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394057908,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "3FOwUTpB",
				"focus": 0.7472541610408855,
				"gap": 11.277596487004843
			},
			"endBinding": {
				"elementId": "bhErD1D1jPguj2_gX1IpG",
				"focus": -0.07538926342461053,
				"gap": 13.793853730722674
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					79.21913449656849,
					-1.2249633422672892
				]
			]
		},
		{
			"type": "line",
			"version": 529,
			"versionNonce": 388047348,
			"isDeleted": false,
			"id": "w-cOvgP0wYwyhmmT0KvqR",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1225.2154904207716,
			"y": 471.26903044632485,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.3875181934722878,
			"height": 9.933649782463025,
			"seed": 1712137076,
			"groupIds": [
				"WZwFAMKZadmBjAFpYFy_C"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.3875181934722878,
					9.933649782463025
				]
			]
		},
		{
			"type": "line",
			"version": 514,
			"versionNonce": 1081157452,
			"isDeleted": false,
			"id": "ZvSVdCT3G-Ngfe5ZOa9N4",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1223.1067608116011,
			"y": 478.5586210161545,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 10.093050375373764,
			"height": 5.352903824739634,
			"seed": 2097190132,
			"groupIds": [
				"WZwFAMKZadmBjAFpYFy_C"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					10.093050375373764,
					5.352903824739634
				]
			]
		},
		{
			"type": "line",
			"version": 526,
			"versionNonce": 403751796,
			"isDeleted": false,
			"id": "eZ4b3ZQrPWJon7lS0kRCg",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1227.5163248077968,
			"y": 479.1558672118935,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 9.445342561429221,
			"height": 4.995069092088584,
			"seed": 394909300,
			"groupIds": [
				"WZwFAMKZadmBjAFpYFy_C"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-9.445342561429221,
					4.995069092088584
				]
			]
		},
		{
			"type": "arrow",
			"version": 647,
			"versionNonce": 217946868,
			"isDeleted": false,
			"id": "bYfWJSc4il4xhySVIU7as",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1349.466641461421,
			"y": 438.4356424518017,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 80.28151527567411,
			"height": 0.9512419290605862,
			"seed": 2116804172,
			"groupIds": [
				"OEAzdryr5bbBfP3Cp8Tpz"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394067227,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "3FOwUTpB",
				"gap": 13.139209443958777,
				"focus": 0.5081890123856795
			},
			"endBinding": {
				"elementId": "JXE81mBAiX_yBu20H-nua",
				"gap": 14.43224077376874,
				"focus": -0.11635036953770762
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					80.28151527567411,
					-0.9512419290605862
				]
			]
		},
		{
			"type": "line",
			"version": 508,
			"versionNonce": 1838167284,
			"isDeleted": false,
			"id": "q2mXpOvDnNRItzCWANgsp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1390.2154904207716,
			"y": 472.51903044632485,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.3875181934722878,
			"height": 9.933649782463025,
			"seed": 70399180,
			"groupIds": [
				"OEAzdryr5bbBfP3Cp8Tpz"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.3875181934722878,
					9.933649782463025
				]
			]
		},
		{
			"type": "line",
			"version": 493,
			"versionNonce": 443597900,
			"isDeleted": false,
			"id": "Tu9ZgrLtt-Z4HTGhcqycb",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1388.1067608116011,
			"y": 479.8086210161545,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 10.093050375373764,
			"height": 5.352903824739634,
			"seed": 1412021068,
			"groupIds": [
				"OEAzdryr5bbBfP3Cp8Tpz"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					10.093050375373764,
					5.352903824739634
				]
			]
		},
		{
			"type": "line",
			"version": 505,
			"versionNonce": 354776692,
			"isDeleted": false,
			"id": "n5GPh3cQDpP7mSYqm11sw",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1392.5163248077968,
			"y": 480.4058672118935,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 9.445342561429221,
			"height": 4.995069092088584,
			"seed": 2020372940,
			"groupIds": [
				"OEAzdryr5bbBfP3Cp8Tpz"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-9.445342561429221,
					4.995069092088584
				]
			]
		},
		{
			"type": "arrow",
			"version": 521,
			"versionNonce": 1609938380,
			"isDeleted": false,
			"id": "x5gL0yqYXkUqAIgEOIsS8",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1606.583394017295,
			"y": 439.3201296539034,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 79.21913449656849,
			"height": 1.2249633422672892,
			"seed": 1144045684,
			"groupIds": [
				"HzfBfdAQPMVv5k4H167Sn"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394096968,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "3FOwUTpB",
				"focus": 0.1318845692916152,
				"gap": 13.584200651556472
			},
			"endBinding": {
				"elementId": "55yF4s8cK8oitbb8-TG-p",
				"focus": -0.05565654207017585,
				"gap": 11.487249566171045
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					79.21913449656849,
					-1.2249633422672892
				]
			]
		},
		{
			"type": "line",
			"version": 504,
			"versionNonce": 1805027316,
			"isDeleted": false,
			"id": "6DN1F_4_QvzFjYA-xONPr",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1646.4654904207716,
			"y": 473.76903044632485,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.3875181934722878,
			"height": 9.933649782463025,
			"seed": 1856541172,
			"groupIds": [
				"HzfBfdAQPMVv5k4H167Sn"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.3875181934722878,
					9.933649782463025
				]
			]
		},
		{
			"type": "line",
			"version": 489,
			"versionNonce": 619520332,
			"isDeleted": false,
			"id": "LlBF23P1lbjglLIpclX4y",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1644.3567608116011,
			"y": 481.0586210161545,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 10.093050375373764,
			"height": 5.352903824739634,
			"seed": 1831482228,
			"groupIds": [
				"HzfBfdAQPMVv5k4H167Sn"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					10.093050375373764,
					5.352903824739634
				]
			]
		},
		{
			"type": "line",
			"version": 501,
			"versionNonce": 1156147572,
			"isDeleted": false,
			"id": "wREQP7o5XjaXHlOMN8qzl",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1648.7663248077968,
			"y": 481.6558672118935,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 9.445342561429221,
			"height": 4.995069092088584,
			"seed": 1039901940,
			"groupIds": [
				"HzfBfdAQPMVv5k4H167Sn"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-9.445342561429221,
					4.995069092088584
				]
			]
		},
		{
			"type": "arrow",
			"version": 585,
			"versionNonce": 1322555724,
			"isDeleted": false,
			"id": "p-qQBHcpZu5v302CP7G7C",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1857.6787906598715,
			"y": 442.53874412033736,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 79.21915710119038,
			"height": 1.2236049638983673,
			"seed": 454953292,
			"groupIds": [
				"bxt2UTyrqgCtO5sMsrdir"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394083811,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "57vYi_hUgZICc95CvsVNT",
				"gap": 8.526967720326752,
				"focus": -0.21883825851032895
			},
			"endBinding": {
				"elementId": "HcfGIx8QfErFfv4db-QC9",
				"gap": 12.244482497400838,
				"focus": -0.1768588426309053
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					79.21915710119038,
					-1.2236049638983673
				]
			]
		},
		{
			"type": "line",
			"version": 528,
			"versionNonce": 73669364,
			"isDeleted": false,
			"id": "UYAWGcQ3ZpNyMAKD4_DDH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1897.7154904207716,
			"y": 476.2690304463249,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.3875181934722878,
			"height": 9.933649782463025,
			"seed": 933691340,
			"groupIds": [
				"bxt2UTyrqgCtO5sMsrdir"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.3875181934722878,
					9.933649782463025
				]
			]
		},
		{
			"type": "line",
			"version": 513,
			"versionNonce": 2008432204,
			"isDeleted": false,
			"id": "PG6f_ShaC2y0htFH-6D1a",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1895.6067608116007,
			"y": 483.5586210161546,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 10.093050375373764,
			"height": 5.352903824739634,
			"seed": 1959601740,
			"groupIds": [
				"bxt2UTyrqgCtO5sMsrdir"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					10.093050375373764,
					5.352903824739634
				]
			]
		},
		{
			"type": "line",
			"version": 525,
			"versionNonce": 881630324,
			"isDeleted": false,
			"id": "G3Ts8my-BM7QKkoj7A5lc",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1900.0163248077968,
			"y": 484.15586721189356,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 9.445342561429221,
			"height": 4.995069092088584,
			"seed": 661290188,
			"groupIds": [
				"bxt2UTyrqgCtO5sMsrdir"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-9.445342561429221,
					4.995069092088584
				]
			]
		},
		{
			"type": "arrow",
			"version": 614,
			"versionNonce": 1717880052,
			"isDeleted": false,
			"id": "4aos56TmvczGt-URyHOe8",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 2246.2139496468417,
			"y": 438.44198460491623,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 79.95377835156523,
			"height": 1.2340462017648974,
			"seed": 1407209716,
			"groupIds": [
				"XLNJu3nIl4I17Rp6zBE0m"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394093062,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "3FOwUTpB",
				"gap": 12.842334732438957,
				"focus": -0.8005258412487583
			},
			"endBinding": {
				"elementId": "M0rA0Ff4JnrhhWQybdRce",
				"gap": 14.10411548528856,
				"focus": -0.26947890027998805
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					79.95377835156523,
					-1.2340462017648974
				]
			]
		},
		{
			"type": "line",
			"version": 515,
			"versionNonce": 522776052,
			"isDeleted": false,
			"id": "LBfq7lWcOcwd1BFQkvkrE",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 2286.465490420772,
			"y": 472.51903044632485,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.3875181934722878,
			"height": 9.933649782463025,
			"seed": 1930564212,
			"groupIds": [
				"XLNJu3nIl4I17Rp6zBE0m"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.3875181934722878,
					9.933649782463025
				]
			]
		},
		{
			"type": "line",
			"version": 500,
			"versionNonce": 1989942092,
			"isDeleted": false,
			"id": "p-qIHy7Vu51Ppgovlfrl8",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 2284.356760811601,
			"y": 479.8086210161545,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 10.093050375373764,
			"height": 5.352903824739634,
			"seed": 428844020,
			"groupIds": [
				"XLNJu3nIl4I17Rp6zBE0m"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					10.093050375373764,
					5.352903824739634
				]
			]
		},
		{
			"type": "line",
			"version": 512,
			"versionNonce": 1698631540,
			"isDeleted": false,
			"id": "O_FSP0nfWzGcrzIgPyluk",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 2288.766324807797,
			"y": 480.4058672118935,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 9.445342561429221,
			"height": 4.995069092088584,
			"seed": 224331124,
			"groupIds": [
				"XLNJu3nIl4I17Rp6zBE0m"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394051074,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-9.445342561429221,
					4.995069092088584
				]
			]
		},
		{
			"type": "rectangle",
			"version": 66,
			"versionNonce": 1408402636,
			"isDeleted": false,
			"id": "G1aiOPkS6EvY-77QNZ5yP",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1037.9928479875837,
			"y": 485.035699026925,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 53.75,
			"height": 104.99999999999994,
			"seed": 757612788,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394119649,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 116,
			"versionNonce": 690624460,
			"isDeleted": false,
			"id": "bhErD1D1jPguj2_gX1IpG",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1199.8678479875837,
			"y": 490.03569902692493,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 53.75,
			"height": 235,
			"seed": 547720140,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "0EBPf3pRnX_Wgj2n2oFoH",
					"type": "arrow"
				},
				{
					"id": "QhJiCuhlIBgp9-8JH9DVf",
					"type": "arrow"
				}
			],
			"updated": 1710394126546,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "rectangle",
			"version": 186,
			"versionNonce": 1150289908,
			"isDeleted": false,
			"id": "JXE81mBAiX_yBu20H-nua",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1364.8678479875837,
			"y": 492.53569902692493,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 53.75,
			"height": 345,
			"seed": 1985275892,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "bYfWJSc4il4xhySVIU7as",
					"type": "arrow"
				}
			],
			"updated": 1710394067227,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "rectangle",
			"version": 248,
			"versionNonce": 1305812044,
			"isDeleted": false,
			"id": "55yF4s8cK8oitbb8-TG-p",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1621.1178479875837,
			"y": 490.03569902692493,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 53.75,
			"height": 409.99999999999994,
			"seed": 534860236,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "x5gL0yqYXkUqAIgEOIsS8",
					"type": "arrow"
				}
			],
			"updated": 1710394096968,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "rectangle",
			"version": 312,
			"versionNonce": 357973068,
			"isDeleted": false,
			"id": "HcfGIx8QfErFfv4db-QC9",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1874.8678479875837,
			"y": 493.78569902692493,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 53.75,
			"height": 481.25,
			"seed": 318655820,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "p-qQBHcpZu5v302CP7G7C",
					"type": "arrow"
				}
			],
			"updated": 1710394083811,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "rectangle",
			"version": 399,
			"versionNonce": 1490661876,
			"isDeleted": false,
			"id": "M0rA0Ff4JnrhhWQybdRce",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2266.1178479875844,
			"y": 491.91069902692493,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 53.75,
			"height": 851.2499999999999,
			"seed": 1873933812,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "4aos56TmvczGt-URyHOe8",
					"type": "arrow"
				}
			],
			"updated": 1710394093062,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "arrow",
			"version": 576,
			"versionNonce": 1404448332,
			"isDeleted": false,
			"id": "vwXIayqzaYnCAEgcxXWZa",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1028.3383863291647,
			"y": 628.9069094016602,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 79.21913449656849,
			"height": 1.2249633422672892,
			"seed": 1856698444,
			"groupIds": [
				"b7gJjXPD8uQVXx4LGuJhE"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394119646,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "aZj9gz3L-Egum3UIulyO8",
				"focus": 0.017518782239512722,
				"gap": 9.603504127037013
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					79.21913449656849,
					-1.2249633422672892
				]
			]
		},
		{
			"type": "line",
			"version": 541,
			"versionNonce": 846231796,
			"isDeleted": false,
			"id": "4z50elcmxuY7EAdLlSds0",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1068.2204827326411,
			"y": 663.3558101940816,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.3875181934722878,
			"height": 9.933649782463025,
			"seed": 163450572,
			"groupIds": [
				"b7gJjXPD8uQVXx4LGuJhE"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394119028,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.3875181934722878,
					9.933649782463025
				]
			]
		},
		{
			"type": "line",
			"version": 526,
			"versionNonce": 1566390900,
			"isDeleted": false,
			"id": "B5861gk3s_RPU_VM3WQ9x",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1066.111753123471,
			"y": 670.6454007639113,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 10.093050375373764,
			"height": 5.352903824739634,
			"seed": 791303500,
			"groupIds": [
				"b7gJjXPD8uQVXx4LGuJhE"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394119028,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					10.093050375373764,
					5.352903824739634
				]
			]
		},
		{
			"type": "line",
			"version": 538,
			"versionNonce": 1614138356,
			"isDeleted": false,
			"id": "jF_m7iXWZfz5bzF_wS4zB",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1070.5213171196663,
			"y": 671.2426469596503,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 9.445342561429221,
			"height": 4.995069092088584,
			"seed": 474598348,
			"groupIds": [
				"b7gJjXPD8uQVXx4LGuJhE"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394119028,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-9.445342561429221,
					4.995069092088584
				]
			]
		},
		{
			"type": "rectangle",
			"version": 131,
			"versionNonce": 1828728180,
			"isDeleted": false,
			"id": "aZj9gz3L-Egum3UIulyO8",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1039.8678479875837,
			"y": 677.1302605709279,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 53.75,
			"height": 104.99999999999994,
			"seed": 1396077132,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "vwXIayqzaYnCAEgcxXWZa",
					"type": "arrow"
				}
			],
			"updated": 1710394119028,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "arrow",
			"version": 577,
			"versionNonce": 1734347596,
			"isDeleted": false,
			"id": "LheR9ZVtV9iNJC_eu3Mcf",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1023.3383863291647,
			"y": 818.9069094016602,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 79.21913449656849,
			"height": 1.2249633422672892,
			"seed": 1710370292,
			"groupIds": [
				"1PixuuiefQepnHync4NEJ"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394119649,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "wAjkQp593zUAZTDcjMgLn",
				"focus": -0.011189089390521089,
				"gap": 9.423114708938556
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					79.21913449656849,
					-1.2249633422672892
				]
			]
		},
		{
			"type": "line",
			"version": 544,
			"versionNonce": 2013671924,
			"isDeleted": false,
			"id": "vtSpcmOjjHVdd7QU7GBY1",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1063.2204827326414,
			"y": 853.3558101940816,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.3875181934722878,
			"height": 9.933649782463025,
			"seed": 14700404,
			"groupIds": [
				"1PixuuiefQepnHync4NEJ"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394119028,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.3875181934722878,
					9.933649782463025
				]
			]
		},
		{
			"type": "line",
			"version": 529,
			"versionNonce": 970183540,
			"isDeleted": false,
			"id": "YFM7F-PE-T5CXSEwpgYT7",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1061.1117531234709,
			"y": 860.6454007639113,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 10.093050375373764,
			"height": 5.352903824739634,
			"seed": 747520244,
			"groupIds": [
				"1PixuuiefQepnHync4NEJ"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394119028,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					10.093050375373764,
					5.352903824739634
				]
			]
		},
		{
			"type": "line",
			"version": 541,
			"versionNonce": 74532084,
			"isDeleted": false,
			"id": "HNYvR8Z_bIBFUf3P-97Z2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1065.5213171196665,
			"y": 861.2426469596503,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 9.445342561429221,
			"height": 4.995069092088584,
			"seed": 1619133044,
			"groupIds": [
				"1PixuuiefQepnHync4NEJ"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394119028,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-9.445342561429221,
					4.995069092088584
				]
			]
		},
		{
			"type": "rectangle",
			"version": 134,
			"versionNonce": 1298433652,
			"isDeleted": false,
			"id": "wAjkQp593zUAZTDcjMgLn",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1034.8678479875837,
			"y": 867.1302605709279,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 53.75,
			"height": 104.99999999999994,
			"seed": 864130036,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "LheR9ZVtV9iNJC_eu3Mcf",
					"type": "arrow"
				}
			],
			"updated": 1710394119028,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "arrow",
			"version": 592,
			"versionNonce": 1982676556,
			"isDeleted": false,
			"id": "QhJiCuhlIBgp9-8JH9DVf",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1191.583394017295,
			"y": 767.5316358983159,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 79.21913449656849,
			"height": 1.2249633422672892,
			"seed": 1855807988,
			"groupIds": [
				"hluSf7o_wLP0vK6ov-iCb"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394126546,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "bhErD1D1jPguj2_gX1IpG",
				"focus": -0.15367098073530247,
				"gap": 2.141041230098722
			},
			"endBinding": {
				"elementId": "dtu7vX5YLP2cDTNM-hnLJ",
				"focus": -0.0921128594075992,
				"gap": 14.341915232041401
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					79.21913449656849,
					-1.2249633422672892
				]
			]
		},
		{
			"type": "line",
			"version": 552,
			"versionNonce": 99897460,
			"isDeleted": false,
			"id": "JDajMYa8FKU5wvta41BNI",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1231.4654904207716,
			"y": 801.9805366907374,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.3875181934722878,
			"height": 9.933649782463025,
			"seed": 906298228,
			"groupIds": [
				"hluSf7o_wLP0vK6ov-iCb"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394125862,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.3875181934722878,
					9.933649782463025
				]
			]
		},
		{
			"type": "line",
			"version": 537,
			"versionNonce": 1366958580,
			"isDeleted": false,
			"id": "mS8pMtE8nZRneQyvHU52x",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1229.3567608116011,
			"y": 809.270127260567,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 10.093050375373764,
			"height": 5.352903824739634,
			"seed": 1123841268,
			"groupIds": [
				"hluSf7o_wLP0vK6ov-iCb"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394125862,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					10.093050375373764,
					5.352903824739634
				]
			]
		},
		{
			"type": "line",
			"version": 549,
			"versionNonce": 524927860,
			"isDeleted": false,
			"id": "rEo9Nautg-0WFOCbUX8eL",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1233.7663248077968,
			"y": 809.867373456306,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 9.445342561429221,
			"height": 4.995069092088584,
			"seed": 1930016372,
			"groupIds": [
				"hluSf7o_wLP0vK6ov-iCb"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394125862,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-9.445342561429221,
					4.995069092088584
				]
			]
		},
		{
			"type": "rectangle",
			"version": 138,
			"versionNonce": 631846132,
			"isDeleted": false,
			"id": "dtu7vX5YLP2cDTNM-hnLJ",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1206.1178479875837,
			"y": 820.7472052713374,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 53.75,
			"height": 235,
			"seed": 49465332,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "QhJiCuhlIBgp9-8JH9DVf",
					"type": "arrow"
				}
			],
			"updated": 1710394125862,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "arrow",
			"version": 684,
			"versionNonce": 660299340,
			"isDeleted": false,
			"id": "-r19A8EoWfNp_hmAQkH3X",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1863.9287906598718,
			"y": 1005.9674221219647,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 79.21915710119038,
			"height": 1.2236049638983673,
			"seed": 1280397812,
			"groupIds": [
				"tNnchh0h3vhvXAGpNQcKC"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394136868,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "3cWqex-VjBV_Rdgm3g3mo",
				"focus": -0.1857567414617679,
				"gap": 12.173271801053033
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					79.21915710119038,
					-1.2236049638983673
				]
			]
		},
		{
			"type": "line",
			"version": 578,
			"versionNonce": 838181748,
			"isDeleted": false,
			"id": "BSQA-Sev_9xtdmbJEs2lb",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1903.9654904207716,
			"y": 1039.6977084479522,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 0.3875181934722878,
			"height": 9.933649782463025,
			"seed": 398127988,
			"groupIds": [
				"tNnchh0h3vhvXAGpNQcKC"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394135779,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.3875181934722878,
					9.933649782463025
				]
			]
		},
		{
			"type": "line",
			"version": 563,
			"versionNonce": 936973556,
			"isDeleted": false,
			"id": "Dvu66EEfLiFfSs3kjEyYX",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1901.8567608116007,
			"y": 1046.9872990177819,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 10.093050375373764,
			"height": 5.352903824739634,
			"seed": 1484023028,
			"groupIds": [
				"tNnchh0h3vhvXAGpNQcKC"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394135779,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					10.093050375373764,
					5.352903824739634
				]
			]
		},
		{
			"type": "line",
			"version": 575,
			"versionNonce": 1666340468,
			"isDeleted": false,
			"id": "sB8Ex28pZNCpukJYfR8s9",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5874356785049004,
			"x": 1906.2663248077968,
			"y": 1047.5845452135209,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 9.445342561429221,
			"height": 4.995069092088584,
			"seed": 1946396276,
			"groupIds": [
				"tNnchh0h3vhvXAGpNQcKC"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710394135779,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-9.445342561429221,
					4.995069092088584
				]
			]
		},
		{
			"type": "rectangle",
			"version": 362,
			"versionNonce": 556230644,
			"isDeleted": false,
			"id": "3cWqex-VjBV_Rdgm3g3mo",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1881.1178479875837,
			"y": 1057.214377028552,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 53.75,
			"height": 481.25,
			"seed": 791590900,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "-r19A8EoWfNp_hmAQkH3X",
					"type": "arrow"
				}
			],
			"updated": 1710394135779,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 113,
			"versionNonce": 1940277708,
			"isDeleted": false,
			"id": "JCGuNedH",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1067.9928479875837,
			"y": 287.535699026925,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"width": 1578.375,
			"height": 43.199999999999996,
			"seed": 608431988,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394230949,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "0  1   2   3   4   5   6   7   8   9  10  11  12    13   14   15    数组下标",
			"rawText": "0  1   2   3   4   5   6   7   8   9  10  11  12    13   14   15    数组下标",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0  1   2   3   4   5   6   7   8   9  10  11  12    13   14   15    数组下标",
			"lineHeight": 1.2
		},
		{
			"type": "text",
			"version": 48,
			"versionNonce": 997606732,
			"isDeleted": false,
			"id": "Fhm7o26I",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2499.242847987584,
			"y": 346.285699026925,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"width": 216,
			"height": 43.199999999999996,
			"seed": 798967500,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710394257752,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "对应的字节数",
			"rawText": "对应的字节数",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "对应的字节数",
			"lineHeight": 1.2
		},
		{
			"type": "rectangle",
			"version": 131,
			"versionNonce": 616535372,
			"isDeleted": false,
			"id": "_G8P3Goz9umfgFUTlywxV",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 329.5761813209167,
			"y": 1698.6190323602582,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 295,
			"height": 103.33333333333348,
			"seed": 1363567180,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "3hnwUTUd"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 83,
			"versionNonce": 758582220,
			"isDeleted": false,
			"id": "3hnwUTUd",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 387.0761813209167,
			"y": 1728.685699026925,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 180,
			"height": 43.199999999999996,
			"seed": 1137933684,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "所需字节数",
			"rawText": "所需字节数",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "_G8P3Goz9umfgFUTlywxV",
			"originalText": "所需字节数",
			"lineHeight": 1.2
		},
		{
			"type": "diamond",
			"version": 256,
			"versionNonce": 2076761553,
			"isDeleted": false,
			"id": "59-Hr5v1lSmfkQqtH6uuA",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 324.5761813209165,
			"y": 1905.2856990269256,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 298.33333333333326,
			"height": 198.3333333333333,
			"seed": 1990595532,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "yWYJdqib"
				},
				{
					"id": "NSan78IgEE2UeZVWJRIkD",
					"type": "arrow"
				},
				{
					"id": "IEIf8MDZpd_dkwojaf_Ir",
					"type": "arrow"
				}
			],
			"updated": 1714358879564,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 206,
			"versionNonce": 1443830577,
			"isDeleted": false,
			"id": "yWYJdqib",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 352.1022229875831,
			"y": 1982.8523656935922,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 243.28125,
			"height": 43.199999999999996,
			"seed": 1037558220,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358879565,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "大于128字节？",
			"rawText": "大于128字节？",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "59-Hr5v1lSmfkQqtH6uuA",
			"originalText": "大于128字节？",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 193,
			"versionNonce": 1469043089,
			"isDeleted": false,
			"id": "NSan78IgEE2UeZVWJRIkD",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 471.24284798758345,
			"y": 1791.9523656935917,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 1.2063969665533705,
			"height": 108.28619171785476,
			"seed": 122425588,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358924748,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "59-Hr5v1lSmfkQqtH6uuA",
				"gap": 5.210282842115518,
				"focus": -0.0008887760284415791
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					1.2063969665533705,
					108.28619171785476
				]
			]
		},
		{
			"type": "rectangle",
			"version": 545,
			"versionNonce": 1290191564,
			"isDeleted": false,
			"id": "I7LG8v3_Hc-PQZEYuAwTw",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": -265.4238186790833,
			"y": 1978.6190323602582,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 383.3333333333334,
			"height": 136.66666666666674,
			"seed": 2080079604,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "7E4wgkDR"
				},
				{
					"id": "IEIf8MDZpd_dkwojaf_Ir",
					"type": "arrow"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 494,
			"versionNonce": 1117863121,
			"isDeleted": false,
			"id": "7E4wgkDR",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": -253.75715201241658,
			"y": 2025.3523656935915,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 360,
			"height": 43.199999999999996,
			"seed": 20592500,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358879566,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "由一级空间配置器申请",
			"rawText": "由一级空间配置器申请",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "I7LG8v3_Hc-PQZEYuAwTw",
			"originalText": "由一级空间配置器申请",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 988,
			"versionNonce": 363200785,
			"isDeleted": false,
			"id": "IEIf8MDZpd_dkwojaf_Ir",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 331.61852778768844,
			"y": 2012.5126679493878,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 210.37567980010493,
			"height": 9.280931614982364,
			"seed": 215476468,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "FF0BCCvl"
				}
			],
			"updated": 1714358924750,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"startBinding": {
				"elementId": "59-Hr5v1lSmfkQqtH6uuA",
				"gap": 2.8135134103166735,
				"focus": -0.018053919454903512
			},
			"endBinding": {
				"elementId": "I7LG8v3_Hc-PQZEYuAwTw",
				"gap": 3.3333333333333144,
				"focus": -0.21560600862340562
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-210.37567980010493,
					9.280931614982364
				]
			]
		},
		{
			"type": "text",
			"version": 17,
			"versionNonce": 974820044,
			"isDeleted": false,
			"id": "FF0BCCvl",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 794.9095146542501,
			"y": 1959.5190323602583,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 1093919988,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710396272941,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "是",
			"rawText": "是",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "IEIf8MDZpd_dkwojaf_Ir",
			"originalText": "是",
			"lineHeight": 1.2
		},
		{
			"type": "rectangle",
			"version": 125,
			"versionNonce": 569965772,
			"isDeleted": false,
			"id": "pIrQY5LxGEHP1yBlWFAXu",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 832.90951465425,
			"y": 1943.6190323602582,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 448.33333333333303,
			"height": 150,
			"seed": 1636794740,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "r8mitfx2CI0DKhWlgWLhg",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "VckFwQxf"
				},
				{
					"id": "mWyfK4BJGzp267DGIM6ry",
					"type": "arrow"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 79,
			"versionNonce": 500663116,
			"isDeleted": false,
			"id": "VckFwQxf",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 931.0761813209165,
			"y": 1997.0190323602583,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 252,
			"height": 43.199999999999996,
			"seed": 2116826060,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "选择要使用的桶",
			"rawText": "选择要使用的桶",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "pIrQY5LxGEHP1yBlWFAXu",
			"originalText": "选择要使用的桶",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 163,
			"versionNonce": 205895409,
			"isDeleted": false,
			"id": "r8mitfx2CI0DKhWlgWLhg",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 616.2428479875832,
			"y": 2001.9523656935917,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 211.66666666666674,
			"height": 6.666666666666515,
			"seed": 120874484,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "0audJkQa"
				}
			],
			"updated": 1714358924751,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"startBinding": null,
			"endBinding": {
				"elementId": "pIrQY5LxGEHP1yBlWFAXu",
				"gap": 5,
				"focus": 0.37230129537821816
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					211.66666666666674,
					-6.666666666666515
				]
			]
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1005871180,
			"isDeleted": false,
			"id": "0audJkQa",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1326.5761813209165,
			"y": 1957.0190323602583,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 1291075956,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710396326475,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "否",
			"rawText": "否",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "r8mitfx2CI0DKhWlgWLhg",
			"originalText": "否",
			"lineHeight": 1.2
		},
		{
			"type": "diamond",
			"version": 408,
			"versionNonce": 507870540,
			"isDeleted": false,
			"id": "yhrWzMpLHAjNGIxikNy_-",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 826.242847987583,
			"y": 2253.619032360258,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 473.333333333333,
			"height": 194,
			"seed": 1152862668,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "3iEsfAzp"
				},
				{
					"id": "mWyfK4BJGzp267DGIM6ry",
					"type": "arrow"
				},
				{
					"id": "6o-ScOP8l4ZlnBPANHfWq",
					"type": "arrow"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 243,
			"versionNonce": 1420360113,
			"isDeleted": false,
			"id": "3iEsfAzp",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 864.9095146542495,
			"y": 2329.0190323602583,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 396,
			"height": 43.199999999999996,
			"seed": 620431564,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358879569,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "该桶下是否已挂上内存块",
			"rawText": "该桶下是否已挂上内存块",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "yhrWzMpLHAjNGIxikNy_-",
			"originalText": "该桶下是否已挂上内存块",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 210,
			"versionNonce": 2030974577,
			"isDeleted": false,
			"id": "mWyfK4BJGzp267DGIM6ry",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1056.2428479875834,
			"y": 2096.9523656935917,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 3.33333333333303,
			"height": 155,
			"seed": 631984332,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358924753,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "pIrQY5LxGEHP1yBlWFAXu",
				"gap": 3.333333333333485,
				"focus": 0.011152121284277883
			},
			"endBinding": {
				"elementId": "yhrWzMpLHAjNGIxikNy_-",
				"gap": 2.8063017678561977,
				"focus": -0.005118885355141154
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					3.33333333333303,
					155
				]
			]
		},
		{
			"type": "rectangle",
			"version": 112,
			"versionNonce": 674344396,
			"isDeleted": false,
			"id": "FhkotQY5o62Vn53gKd9_I",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 277.9095146542502,
			"y": 2268.619032360258,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 346.6666666666665,
			"height": 186.66666666666697,
			"seed": 426689140,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "oy8ZfBAC"
				},
				{
					"id": "6o-ScOP8l4ZlnBPANHfWq",
					"type": "arrow"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 150,
			"versionNonce": 466752588,
			"isDeleted": false,
			"id": "oy8ZfBAC",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 307.24284798758345,
			"y": 2318.752365693592,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 288,
			"height": 86.39999999999999,
			"seed": 104742772,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "将桶上第一个小块\n内存返回给用户",
			"rawText": "将桶上第一个小块\n内存返回给用户",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "FhkotQY5o62Vn53gKd9_I",
			"originalText": "将桶上第一个小块\n内存返回给用户",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 229,
			"versionNonce": 1943729649,
			"isDeleted": false,
			"id": "6o-ScOP8l4ZlnBPANHfWq",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 826.2428479875832,
			"y": 2351.9523656935917,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 200,
			"height": 3.333333333333485,
			"seed": 444117620,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "TkScQM6P"
				}
			],
			"updated": 1714358924754,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"startBinding": {
				"elementId": "yhrWzMpLHAjNGIxikNy_-",
				"gap": 1.2337301889647279,
				"focus": -0.05441008018327932
			},
			"endBinding": {
				"elementId": "FhkotQY5o62Vn53gKd9_I",
				"gap": 1.666666666666515,
				"focus": -0.1688799076212495
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-200,
					-3.333333333333485
				]
			]
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 122960844,
			"isDeleted": false,
			"id": "TkScQM6P",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1330.7428479875834,
			"y": 2308.685699026925,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 1215905268,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710396454283,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "是",
			"rawText": "是",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "6o-ScOP8l4ZlnBPANHfWq",
			"originalText": "是",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 146,
			"versionNonce": 1170804689,
			"isDeleted": false,
			"id": "5kaGlqex3D6-U7guZ7AVW",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1062.90951465425,
			"y": 2441.9523656935917,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 3.333333333333485,
			"height": 143.33333333333303,
			"seed": 2062530892,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "8jBNNBdC"
				}
			],
			"updated": 1714358924756,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"startBinding": null,
			"endBinding": {
				"elementId": "ZENk80MuUwxsgQSgA-WRa",
				"gap": 4.999999999999773,
				"focus": -0.04437742352434244
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					3.333333333333485,
					143.33333333333303
				]
			]
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 85430388,
			"isDeleted": false,
			"id": "8jBNNBdC",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1669.0761813209167,
			"y": 2472.0190323602583,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 815638988,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710396499352,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "否",
			"rawText": "否",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "5kaGlqex3D6-U7guZ7AVW",
			"originalText": "否",
			"lineHeight": 1.2
		},
		{
			"type": "rectangle",
			"version": 97,
			"versionNonce": 1441762892,
			"isDeleted": false,
			"id": "ZENk80MuUwxsgQSgA-WRa",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 856.2428479875834,
			"y": 2590.2856990269247,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 445,
			"height": 206.66666666666652,
			"seed": 1273669196,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "5kaGlqex3D6-U7guZ7AVW",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "s6X9W0N2"
				},
				{
					"id": "3Oqc0bNkB2-SYWEMm-uak",
					"type": "arrow"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 99,
			"versionNonce": 134210764,
			"isDeleted": false,
			"id": "s6X9W0N2",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 916.7428479875834,
			"y": 2672.019032360258,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 324,
			"height": 43.199999999999996,
			"seed": 1617874420,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "向桶中填充小块内存",
			"rawText": "向桶中填充小块内存",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ZENk80MuUwxsgQSgA-WRa",
			"originalText": "向桶中填充小块内存",
			"lineHeight": 1.2
		},
		{
			"type": "rectangle",
			"version": 227,
			"versionNonce": 1073859345,
			"isDeleted": false,
			"id": "gjj9XTuZZVfhk-UQoMlVU",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2136.5761813209165,
			"y": 1938.6190323602577,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 508.33333333333286,
			"height": 183,
			"seed": 726162164,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "EdE4Bttr"
				},
				{
					"id": "SlWB5DU-XeEYRwLKbWY94",
					"type": "arrow"
				}
			],
			"updated": 1714358879573,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 314,
			"versionNonce": 1186953393,
			"isDeleted": false,
			"id": "EdE4Bttr",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2156.742847987583,
			"y": 1965.3190323602578,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 468,
			"height": 129.6,
			"seed": 2108697076,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358879573,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "计算 num 个 n\n字节大小的内存块所需的大小\n以及内存池的剩余空间",
			"rawText": "计算 num 个 n 字节大小的内存块所需的大小以及内存池的剩余空间",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "gjj9XTuZZVfhk-UQoMlVU",
			"originalText": "计算 num 个 n 字节大小的内存块所需的大小以及内存池的剩余空间",
			"lineHeight": 1.2
		},
		{
			"type": "diamond",
			"version": 230,
			"versionNonce": 1529749329,
			"isDeleted": false,
			"id": "LQQeS1MDVHbilTyaDqiIl",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2041.5761813209174,
			"y": 2229.6190323602577,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 383.3333333333336,
			"height": 194,
			"seed": 1378017740,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "D6NKNDmz"
				},
				{
					"id": "kEd31RKOXDD71m2fo2Sl5",
					"type": "arrow"
				}
			],
			"updated": 1714358924758,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 200,
			"versionNonce": 1790515249,
			"isDeleted": false,
			"id": "D6NKNDmz",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2090.5084729875844,
			"y": 2305.019032360258,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 285.46875,
			"height": 43.199999999999996,
			"seed": 1691123788,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358879574,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "能否提供 num 块",
			"rawText": "能否提供 num 块",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "LQQeS1MDVHbilTyaDqiIl",
			"originalText": "能否提供 num 块",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 238,
			"versionNonce": 531631409,
			"isDeleted": false,
			"id": "kEd31RKOXDD71m2fo2Sl5",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2226.576181320917,
			"y": 2118.6190323602577,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 0,
			"height": 110,
			"seed": 1873901260,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358924758,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "LQQeS1MDVHbilTyaDqiIl",
				"gap": 3.9025986200573044,
				"focus": -0.0347826086956561
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					110
				]
			]
		},
		{
			"type": "diamond",
			"version": 270,
			"versionNonce": 1031356177,
			"isDeleted": false,
			"id": "oJPQsYCDVu4GcsPFI1axZ",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2038.2428479875825,
			"y": 2581.6190323602577,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 383.3333333333336,
			"height": 194,
			"seed": 632958668,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "1e8yJMaw"
				}
			],
			"updated": 1714358924760,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 252,
			"versionNonce": 298867153,
			"isDeleted": false,
			"id": "1e8yJMaw",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2061.7220146542495,
			"y": 2657.019032360258,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 336.375,
			"height": 43.199999999999996,
			"seed": 916616524,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358879576,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "能否提供 至少 1 块",
			"rawText": "能否提供 至少 1 块",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "oJPQsYCDVu4GcsPFI1axZ",
			"originalText": "能否提供 至少 1 块",
			"lineHeight": 1.2
		},
		{
			"type": "rectangle",
			"version": 208,
			"versionNonce": 1670157004,
			"isDeleted": false,
			"id": "QH35B4qo1evesTTkGMaAW",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1664.9095146542504,
			"y": 2271.9523656935917,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 169.99999999999955,
			"height": 463.33333333333303,
			"seed": 520754932,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "UNNAlAPQ"
				},
				{
					"id": "bm3Uzpzh2bRvaB6M5erG1",
					"type": "arrow"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 162,
			"versionNonce": 2142165393,
			"isDeleted": false,
			"id": "UNNAlAPQ",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1677.9095146542502,
			"y": 2460.4190323602584,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 144,
			"height": 86.39999999999999,
			"seed": 510231156,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358879577,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "切割并返\n回空间",
			"rawText": "切割并返回空间",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "QH35B4qo1evesTTkGMaAW",
			"originalText": "切割并返回空间",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 147,
			"versionNonce": 1944286796,
			"isDeleted": false,
			"id": "_UB4slsTX6PDWyF9ZJI3a",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2048.2428479875834,
			"y": 2328.6190323602577,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 216.66666666666652,
			"height": 1.6666666666667425,
			"seed": 686713588,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "ESW5bqim"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-216.66666666666652,
					-1.6666666666667425
				]
			]
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1711799028,
			"isDeleted": false,
			"id": "ESW5bqim",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2512.4095146542504,
			"y": 1976.1856990269248,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 462636876,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710396875203,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "是",
			"rawText": "是",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "_UB4slsTX6PDWyF9ZJI3a",
			"originalText": "是",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 235,
			"versionNonce": 318846193,
			"isDeleted": false,
			"id": "bm3Uzpzh2bRvaB6M5erG1",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2041.576181320917,
			"y": 2676.952365693591,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 201.6666666666663,
			"height": 1.666666666666515,
			"seed": 445775052,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "Qac63gLA"
				}
			],
			"updated": 1714358924761,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"startBinding": null,
			"endBinding": {
				"elementId": "QH35B4qo1evesTTkGMaAW",
				"gap": 5.000000000000455,
				"focus": 0.7563129816241834
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-201.6666666666663,
					1.666666666666515
				]
			]
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1963217484,
			"isDeleted": false,
			"id": "Qac63gLA",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2513.2428479875834,
			"y": 2326.185699026925,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 1726934900,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710396879481,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "是",
			"rawText": "是",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "bm3Uzpzh2bRvaB6M5erG1",
			"originalText": "是",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 154,
			"versionNonce": 1121669964,
			"isDeleted": false,
			"id": "_ZtHErHxibT0dW7j7POR5",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2229.90951465425,
			"y": 2416.9523656935917,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 0,
			"height": 165,
			"seed": 305216372,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "A119Ajtr"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					165
				]
			]
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1507643212,
			"isDeleted": false,
			"id": "A119Ajtr",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2802.40951465425,
			"y": 2147.8523656935918,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 2131952244,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710396925008,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "否",
			"rawText": "否",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "_ZtHErHxibT0dW7j7POR5",
			"originalText": "否",
			"lineHeight": 1.2
		},
		{
			"type": "rectangle",
			"version": 398,
			"versionNonce": 1294666188,
			"isDeleted": false,
			"id": "ytbgaSSwggHM3Smfwg_CP",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2166.576181320917,
			"y": 2926.9523656935917,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 451.66666666666606,
			"height": 183,
			"seed": 1250987380,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "jCyiP4tp"
				},
				{
					"id": "9S3B8paVYSmgiZxMsyqhd",
					"type": "arrow"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 475,
			"versionNonce": 289402956,
			"isDeleted": false,
			"id": "jCyiP4tp",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2173.31576465425,
			"y": 2932.0523656935916,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 438.1875,
			"height": 172.79999999999998,
			"seed": 1095588340,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "内存池空间不足，最小的 n\n大小的内存块都不能提供。\n将内存池中剩余内存挂接到\n桶中",
			"rawText": "内存池空间不足，最小的 n    大小的内存块都不能提供。\n将内存池中剩余内存挂接到桶中",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ytbgaSSwggHM3Smfwg_CP",
			"originalText": "内存池空间不足，最小的 n    大小的内存块都不能提供。\n将内存池中剩余内存挂接到桶中",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 226,
			"versionNonce": 1137667793,
			"isDeleted": false,
			"id": "9S3B8paVYSmgiZxMsyqhd",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2231.576181320917,
			"y": 2770.2856990269247,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 5,
			"height": 151.66666666666697,
			"seed": 1211320052,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "ZN5dJHNv"
				}
			],
			"updated": 1714358924762,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"startBinding": null,
			"endBinding": {
				"elementId": "ytbgaSSwggHM3Smfwg_CP",
				"gap": 5,
				"focus": -0.738539599206095
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-5,
					151.66666666666697
				]
			]
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1359584884,
			"isDeleted": false,
			"id": "ZN5dJHNv",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2801.576181320917,
			"y": 2494.5190323602583,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 1765866444,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710397124912,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "否",
			"rawText": "否",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "9S3B8paVYSmgiZxMsyqhd",
			"originalText": "否",
			"lineHeight": 1.2
		},
		{
			"type": "rectangle",
			"version": 220,
			"versionNonce": 205547857,
			"isDeleted": false,
			"id": "5Qyw772HWBvc88UIcbLKl",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2513.2428479875844,
			"y": 2651.9523656935917,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 431.6666666666665,
			"height": 133.33333333333303,
			"seed": 720334796,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "9zXHAx01"
				},
				{
					"id": "oBffw3Pwcle1HZ3yAsPpX",
					"type": "arrow"
				}
			],
			"updated": 1714358879580,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 247,
			"versionNonce": 402636529,
			"isDeleted": false,
			"id": "9zXHAx01",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2531.0761813209174,
			"y": 2675.4190323602584,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 396,
			"height": 86.39999999999999,
			"seed": 1080052044,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358879580,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "通过系统堆向内存池中补\n充内存",
			"rawText": "通过系统堆向内存池中补充内存",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "5Qyw772HWBvc88UIcbLKl",
			"originalText": "通过系统堆向内存池中补充内存",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 128,
			"versionNonce": 186271564,
			"isDeleted": false,
			"id": "XnnGJQmKQ5tvbFyDYqZUO",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2579.9095146542504,
			"y": 2930.2856990269247,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 0,
			"height": 150,
			"seed": 374761804,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					-150
				]
			]
		},
		{
			"type": "diamond",
			"version": 319,
			"versionNonce": 2087499985,
			"isDeleted": false,
			"id": "5ALydxLwd6xrCQUiF1_22",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2543.2428479875834,
			"y": 2371.9523656935917,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 368.3333333333335,
			"height": 176.66666666666697,
			"seed": 12922828,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "i6Z7FOT6"
				},
				{
					"id": "oBffw3Pwcle1HZ3yAsPpX",
					"type": "arrow"
				},
				{
					"id": "J6329UCyeHqnjk0Uq-vIi",
					"type": "arrow"
				}
			],
			"updated": 1714358879581,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 285,
			"versionNonce": 37046353,
			"isDeleted": false,
			"id": "i6Z7FOT6",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2655.4095146542504,
			"y": 2438.6856990269252,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 144,
			"height": 43.199999999999996,
			"seed": 632639988,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358879581,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "补充成功",
			"rawText": "补充成功",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "5ALydxLwd6xrCQUiF1_22",
			"originalText": "补充成功",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 429,
			"versionNonce": 1603075665,
			"isDeleted": false,
			"id": "oBffw3Pwcle1HZ3yAsPpX",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2735.572381625957,
			"y": 2648.6190323602577,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 2.0463118473380746,
			"height": 96.80251060263754,
			"seed": 1186764532,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358924766,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "5Qyw772HWBvc88UIcbLKl",
				"gap": 3.3333333333339397,
				"focus": 0.03671440500298533
			},
			"endBinding": {
				"elementId": "5ALydxLwd6xrCQUiF1_22",
				"gap": 5.528218199794168,
				"focus": -0.022705963882435946
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-2.0463118473380746,
					-96.80251060263754
				]
			]
		},
		{
			"type": "line",
			"version": 125,
			"versionNonce": 956784204,
			"isDeleted": false,
			"id": "wc2CcXuImklCNX2YdLIvI",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2549.9095146542504,
			"y": 2468.619032360258,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 55,
			"height": 1.666666666666515,
			"seed": 768024780,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-55,
					-1.666666666666515
				]
			]
		},
		{
			"type": "arrow",
			"version": 270,
			"versionNonce": 316345393,
			"isDeleted": false,
			"id": "J6329UCyeHqnjk0Uq-vIi",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2493.2906948775353,
			"y": 2460.285699026925,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 6.6188197767151,
			"height": 341.66666666666697,
			"seed": 368997324,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "I2nxtDD7"
				}
			],
			"updated": 1714358924766,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"startBinding": {
				"elementId": "5ALydxLwd6xrCQUiF1_22",
				"gap": 21.602596757077123,
				"focus": -1.2712334105522984
			},
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					6.6188197767151,
					-341.66666666666697
				]
			]
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 772701684,
			"isDeleted": false,
			"id": "I2nxtDD7",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 3070.7428479875834,
			"y": 1941.185699026925,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 1220555852,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710397327094,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "是",
			"rawText": "是",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "J6329UCyeHqnjk0Uq-vIi",
			"originalText": "是",
			"lineHeight": 1.2
		},
		{
			"type": "rectangle",
			"version": 179,
			"versionNonce": 774191948,
			"isDeleted": false,
			"id": "sEtJkTKtoxYZbZV9IZqiM",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 3091.5761813209165,
			"y": 2396.9523656935917,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 405,
			"height": 161.66666666666652,
			"seed": 625879116,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "kHlwu3ga"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 166,
			"versionNonce": 116912588,
			"isDeleted": false,
			"id": "kHlwu3ga",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 3114.0761813209165,
			"y": 2434.585699026925,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 360,
			"height": 86.39999999999999,
			"seed": 189659084,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "从哈希桶中大块的桶中\n取出内存块补充",
			"rawText": "从哈希桶中大块的桶中取出内存块补充",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "sEtJkTKtoxYZbZV9IZqiM",
			"originalText": "从哈希桶中大块的桶中取出内存块补充",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 141,
			"versionNonce": 1362090060,
			"isDeleted": false,
			"id": "B6AsYJvXpqVHyu8zp0kAP",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2909.90951465425,
			"y": 2460.2856990269247,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 185,
			"height": 1.666666666666515,
			"seed": 1789618292,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "KvVPwkwG"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					185,
					-1.666666666666515
				]
			]
		},
		{
			"type": "text",
			"version": 10,
			"versionNonce": 181664500,
			"isDeleted": false,
			"id": "KvVPwkwG",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 3574.90951465425,
			"y": 2107.8523656935918,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 1283524300,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710397408058,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "否",
			"rawText": "否",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "B6AsYJvXpqVHyu8zp0kAP",
			"originalText": "否",
			"lineHeight": 1.2
		},
		{
			"type": "diamond",
			"version": 395,
			"versionNonce": 233444913,
			"isDeleted": false,
			"id": "zUSrm02n_WZYzyus2CHZc",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 3109.0761813209156,
			"y": 2108.619032360258,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 368.3333333333335,
			"height": 176.66666666666697,
			"seed": 984861172,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "rjfDGJtN"
				},
				{
					"id": "VQeVZbmZ2VIYA9bjHTSj4",
					"type": "arrow"
				}
			],
			"updated": 1714358879584,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 361,
			"versionNonce": 520945137,
			"isDeleted": false,
			"id": "rjfDGJtN",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 3221.2428479875825,
			"y": 2175.3523656935918,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 144,
			"height": 43.199999999999996,
			"seed": 51276660,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358879584,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "补充成功",
			"rawText": "补充成功",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "zUSrm02n_WZYzyus2CHZc",
			"originalText": "补充成功",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 213,
			"versionNonce": 820796945,
			"isDeleted": false,
			"id": "VQeVZbmZ2VIYA9bjHTSj4",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 3301.5761813209165,
			"y": 2403.619032360258,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 1.6666666666669698,
			"height": 113.33333333333348,
			"seed": 382463476,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358924769,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "zUSrm02n_WZYzyus2CHZc",
				"gap": 7.39135692887622,
				"focus": -0.028746340165030103
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-1.6666666666669698,
					-113.33333333333348
				]
			]
		},
		{
			"type": "rectangle",
			"version": 149,
			"versionNonce": 1447241932,
			"isDeleted": false,
			"id": "x7m829K6Mdwdk-D6YmUZ2",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 3093.242847987584,
			"y": 1880.2856990269247,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 388.33333333333303,
			"height": 145,
			"seed": 677047284,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "V9bbn86i"
				},
				{
					"id": "SlWB5DU-XeEYRwLKbWY94",
					"type": "arrow"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 167,
			"versionNonce": 536620876,
			"isDeleted": false,
			"id": "V9bbn86i",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 3107.4095146542504,
			"y": 1909.5856990269247,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 360,
			"height": 86.39999999999999,
			"seed": 1329086068,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "向一级空间配置器申请\n补充",
			"rawText": "向一级空间配置器申请补充",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "x7m829K6Mdwdk-D6YmUZ2",
			"originalText": "向一级空间配置器申请补充",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 111,
			"versionNonce": 1222233164,
			"isDeleted": false,
			"id": "lp8agtJ16jCuGU3qY1Nby",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 3293.2428479875834,
			"y": 2113.619032360258,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 1.666666666666515,
			"height": 91.66666666666674,
			"seed": 1176898932,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "CbWWZ13I"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					1.666666666666515,
					-91.66666666666674
				]
			]
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 617333708,
			"isDeleted": false,
			"id": "CbWWZ13I",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 3866.5761813209165,
			"y": 1716.1856990269248,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 330839540,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710398856106,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "否",
			"rawText": "否",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "lp8agtJ16jCuGU3qY1Nby",
			"originalText": "否",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 338,
			"versionNonce": 507956689,
			"isDeleted": false,
			"id": "SlWB5DU-XeEYRwLKbWY94",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 3091.5761813209174,
			"y": 1973.6190323602586,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 445.0000000000009,
			"height": 6.66666666666697,
			"seed": 2143138420,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358924770,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "x7m829K6Mdwdk-D6YmUZ2",
				"gap": 1.6666666666669698,
				"focus": -0.31517735193079993
			},
			"endBinding": {
				"elementId": "gjj9XTuZZVfhk-UQoMlVU",
				"gap": 1.6666666666669698,
				"focus": -0.7029793755689856
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-445.0000000000009,
					-6.66666666666697
				]
			]
		},
		{
			"type": "line",
			"version": 149,
			"versionNonce": 45361484,
			"isDeleted": false,
			"id": "zrizF29ky8bnX4d3F7drd",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 3108.2428479875834,
			"y": 2193.619032360258,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 490,
			"height": 1.6666666666667425,
			"seed": 1013699316,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-490,
					-1.6666666666667425
				]
			]
		},
		{
			"type": "arrow",
			"version": 123,
			"versionNonce": 125378508,
			"isDeleted": false,
			"id": "6dDMcY62cXx3hxvaRsHrW",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2616.5761813209165,
			"y": 2195.2856990269247,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 0,
			"height": 80,
			"seed": 635784908,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					-80
				]
			]
		},
		{
			"type": "text",
			"version": 100,
			"versionNonce": 1163609676,
			"isDeleted": false,
			"id": "GIUbYFlH",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 2869.90951465425,
			"y": 2188.619032360258,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffc9c9",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 873619276,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "是",
			"rawText": "是",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "是",
			"lineHeight": 1.2
		},
		{
			"type": "diamond",
			"version": 144,
			"versionNonce": 20225228,
			"isDeleted": false,
			"id": "B-jDWY7y89l9uk4KfkCPS",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 904.5761813209167,
			"y": 2893.6190323602586,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 321.6666666666665,
			"height": 194,
			"seed": 1355763148,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "jwdTwWwB"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 88,
			"versionNonce": 1450835313,
			"isDeleted": false,
			"id": "jwdTwWwB",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 939.40951465425,
			"y": 2969.0190323602587,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 252,
			"height": 43.199999999999996,
			"seed": 450993996,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358879586,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "只填充了一块？",
			"rawText": "只填充了一块？",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "B-jDWY7y89l9uk4KfkCPS",
			"originalText": "只填充了一块？",
			"lineHeight": 1.2
		},
		{
			"type": "rectangle",
			"version": 80,
			"versionNonce": 368368076,
			"isDeleted": false,
			"id": "lCsJo7lzO2zkLQKbuun83",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 387.90951465424996,
			"y": 2903.6190323602586,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 318.33333333333326,
			"height": 170,
			"seed": 1278040052,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "TKfsLjop"
				},
				{
					"id": "ZVm1eAL-5ZMJ3H22RH1lT",
					"type": "arrow"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 113,
			"versionNonce": 263984433,
			"isDeleted": false,
			"id": "TKfsLjop",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 403.0761813209166,
			"y": 2945.419032360259,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 288,
			"height": 86.39999999999999,
			"seed": 96525940,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358879588,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "直接将该块内存返\n回给用户",
			"rawText": "直接将该块内存返回给用户",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "lCsJo7lzO2zkLQKbuun83",
			"originalText": "直接将该块内存返回给用户",
			"lineHeight": 1.2
		},
		{
			"type": "rectangle",
			"version": 92,
			"versionNonce": 1589921553,
			"isDeleted": false,
			"id": "etuOAFeSZQ6v8C1FPfzmB",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 832.90951465425,
			"y": 3215.2856990269247,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 526.6666666666665,
			"height": 173.33333333333348,
			"seed": 2145222004,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "m3lF7tWD"
				}
			],
			"updated": 1714358879589,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			}
		},
		{
			"type": "text",
			"version": 130,
			"versionNonce": 1705721073,
			"isDeleted": false,
			"id": "m3lF7tWD",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 844.2428479875832,
			"y": 3258.7523656935914,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 504,
			"height": 86.39999999999999,
			"seed": 1975885132,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358879589,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "将第一块内存返回给用户，剩余\n内存挂入桶中",
			"rawText": "将第一块内存返回给用户，剩余内存挂入桶中",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "etuOAFeSZQ6v8C1FPfzmB",
			"originalText": "将第一块内存返回给用户，剩余内存挂入桶中",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 87,
			"versionNonce": 1748449868,
			"isDeleted": false,
			"id": "lh1BlemJ8Cgviy0pQWxcR",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1062.90951465425,
			"y": 2793.6190323602586,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 0,
			"height": 105,
			"seed": 1622954700,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					105
				]
			]
		},
		{
			"type": "arrow",
			"version": 134,
			"versionNonce": 145681329,
			"isDeleted": false,
			"id": "ZVm1eAL-5ZMJ3H22RH1lT",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 907.90951465425,
			"y": 2991.9523656935917,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 200,
			"height": 3.33333333333303,
			"seed": 1327178100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "0US48Ksk"
				}
			],
			"updated": 1714358924773,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"startBinding": null,
			"endBinding": {
				"elementId": "lCsJo7lzO2zkLQKbuun83",
				"gap": 1.6666666666667425,
				"focus": -0.03058152432260861
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-200,
					-3.33333333333303
				]
			]
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 562331892,
			"isDeleted": false,
			"id": "0US48Ksk",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1412.40951465425,
			"y": 2948.6856990269252,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 1402315084,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399039585,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "是",
			"rawText": "是",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ZVm1eAL-5ZMJ3H22RH1lT",
			"originalText": "是",
			"lineHeight": 1.2
		},
		{
			"type": "arrow",
			"version": 78,
			"versionNonce": 1074665292,
			"isDeleted": false,
			"id": "Jx9h9EHBOgv4C8bK02zfI",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1062.90951465425,
			"y": 3076.9523656935917,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 3.3333333333332575,
			"height": 145,
			"seed": 1420477772,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "jaaFqsdf"
				}
			],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"customData": {
				"legacyTextWrap": true
			},
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-3.3333333333332575,
					145
				]
			]
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 53448308,
			"isDeleted": false,
			"id": "jaaFqsdf",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1665.7428479875834,
			"y": 3107.8523656935918,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#b2f2bb",
			"width": 36,
			"height": 43.199999999999996,
			"seed": 1706953676,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399043582,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "否",
			"rawText": "否",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Jx9h9EHBOgv4C8bK02zfI",
			"originalText": "否",
			"lineHeight": 1.2
		},
		{
			"type": "rectangle",
			"version": 119,
			"versionNonce": 526732748,
			"isDeleted": false,
			"id": "j-9EEhSSjC7KO6HQ6_05W",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1581.9095146542495,
			"y": 1812.6190323602586,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 1994,
			"height": 1366,
			"seed": 1301076852,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 137,
			"versionNonce": 1251536305,
			"isDeleted": false,
			"id": "3Oqc0bNkB2-SYWEMm-uak",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1541.9095146542495,
			"y": 2666.6190323602586,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 209.99999999999977,
			"height": 2,
			"seed": 1896118900,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1714358924756,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "ZENk80MuUwxsgQSgA-WRa",
				"gap": 30.666666666666288,
				"focus": -0.21420937758710673
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-209.99999999999977,
					2
				]
			]
		},
		{
			"type": "text",
			"version": 74,
			"versionNonce": 1919765196,
			"isDeleted": false,
			"id": "GdPBLNmc",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 2,
			"opacity": 60,
			"angle": 0,
			"x": 1683.9095146542495,
			"y": 1850.6190323602586,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 144,
			"height": 43.199999999999996,
			"seed": 111728116,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710399208257,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "填充流程",
			"rawText": "填充流程",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "填充流程",
			"lineHeight": 1.2
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1e1e1e",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 2,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 760.4417920793812,
		"scrollY": -124.31080704364422,
		"zoom": {
			"value": 0.35000000000000003
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		},
		"objectsSnapModeEnabled": false
	},
	"files": {}
}
```
%%