// 通过读取本地配置文件，进行设置默认信息
function getInitConfig(callback) {
  fetch(`../../live2dExtraConfig.json`)
    .then(response => response.json())
    .then(function (myJson) {
      callback && callback(myJson)
    })
    .catch(e => {
      callback && callback()
    });
}

var 溜冰场;

// ExtraInfo 是远程维护的配置信息
getInitConfig((ExtraInfo) => {
  if (ExtraInfo) {
    const list = ExtraInfo["溜冰场"];
    if (Array.isArray(list) && list.length > 0) {
      溜冰场 = list;
    }
  }
})

var 引流 = [
  "https://www.luogu.com.cn/"
]

const initConfig = {
  mode: "fixed",
  hidden: false,
  content: {
    link: 引流,
    welcome: ["Hi！准备好开始今天的算法学习了吗？"],
    touch: "别戳我啦~专心写代码吧！",
    home: ["这里有很多好听的", "边听音乐边刷题？效率满满哦"],
    skin: ["诶，想换个心情继续学习吗？", "换个形象，换种心情，加油！"],
    background: ["要换一个思路吗？", "出去走走，让思路更清晰吧！", "好的环境能让学习更高效哦~",],
  },
  model: [
    "./models/Diana/Diana.model3.json",
    "./models/Ava/Ava.model3.json",
  ],
  tips: true,
  onModelLoad: onModelLoad
}

function updateGod() {
  pio_reference = new Paul_Pio(initConfig)

  pio_alignment = "left"

  // Then apply style
  pio_refresh_style()
}

function reSizeLive2d() {
  const defaultWidth = 280; // 默认宽度280px , zoom = 1
  const container = document.getElementById("pio-container");
  if (container)
    container.style.zoom = Math.round(window.innerWidth / defaultWidth * 100) / 100;
}

window.addEventListener("resize", reSizeLive2d);

function onModelLoad(model) {
  const container = document.getElementById("pio-container")
  reSizeLive2d(); // 初始加载
  const canvas = document.getElementById("pio")
  const modelNmae = model.internalModel.settings.name
  const coreModel = model.internalModel.coreModel
  const motionManager = model.internalModel.motionManager

  let touchList = [
    {
      text: "点击展示文本1",
      motion: "Idle"
    },
    {
      text: "点击展示文本2",
      motion: "Idle"
    }
  ]

  function playAction(action) {
    action.text && pio_reference.modules.render(action.text)
    action.motion && pio_reference.model.motion(action.motion)

    if (action.from && action.to) {
      Object.keys(action.from).forEach(id => {
        const hidePartIndex = coreModel._partIds.indexOf(id)
        TweenLite.to(coreModel._partOpacities, 0.6, { [hidePartIndex]: action.from[id] });
        // coreModel._partOpacities[hidePartIndex] = action.from[id]
      })

      motionManager.once("motionFinish", (data) => {
        Object.keys(action.to).forEach(id => {
          const hidePartIndex = coreModel._partIds.indexOf(id)
          TweenLite.to(coreModel._partOpacities, 0.6, { [hidePartIndex]: action.to[id] });
          // coreModel._partOpacities[hidePartIndex] = action.to[id]
        })
      })
    }
  }

  window.live2d_playAction = playAction; // 挂载到window上，方便调用

  canvas.onclick = function () {
    if (motionManager.state.currentGroup !== "Idle") return

    const action = pio_reference.modules.rand(touchList)
    playAction(action)
  }

  if (modelNmae === "Diana") {
    container.dataset.model = "Diana"
    initConfig.content.skin[1] = ["我是吃货担当 嘉然 Diana~"]
    playAction({ motion: "Tap抱阿草-左手" })

    touchList = [
      {
        text: "这道题不难的，再想想！你一定可以的！",
        motion: "Tap生气 -领结"
      },
      {
        text: "别急别急，慢慢来，算法需要耐心哦~",
        motion: "Tap= =  左蝴蝶结"
      },
      {
        text: "呜呜...这题好难...但我会陪着你的！",
        motion: "Tap哭 -眼角"
      },
      {
        text: "今天的学习进度很棒呢！继续保持！",
        motion: "Tap害羞-中间刘海"
      },
      {
        text: "休息一下也没关系哦，劳逸结合效率更高~",
        motion: "Tap抱阿草-左手"
      },
      {
        text: "不要再戳啦！我要专心给你加油了！",
        motion: "Tap摇头- 身体"
      },
      {
        text: "哇！你又学会了一个新算法！太厉害了！",
        motion: "Tap耳朵-发卡"
      },
      {
        text: "zzZ...你也该休息会儿啦~",
        motion: "Leave"
      },
      {
        text: "做出来了？就知道你超棒的！",
        motion: "Tap右头发"
      },
    ]

  } else if (modelNmae === "Ava") {
    container.dataset.model = "Ava"
    initConfig.content.skin[1] = ["我是<s>拉胯</s>Gamer担当 向晚 AvA~"]
    playAction({
      motion: "Tap左眼",
      from: {
        "Part15": 1
      },
      to: {
        "Part15": 0
      }
    })

    touchList = [
      {
        text: "动态规划？小意思！你肯定能搞定！",
        motion: "Tap右手"
      },
      {
        text: "每解出一道题，你就离大神更近一步！",
        motion: "Tap胸口项链",
        from: {
          "Part12": 1
        },
        to: {
          "Part12": 0
        }
      },
      {
        text: "好...好朋友之间互相鼓励很正常啦，你是最棒的！",
        motion: "Tap中间刘海",
        from: {
          "Part12": 1
        },
        to: {
          "Part12": 0
        }
      },
      {
        text: "啊啊啊！这个算法太巧妙了吧！",
        motion: "Tap右眼",
        from: {
          "Part16": 1
        },
        to: {
          "Part16": 0
        }
      },
      {
        text: "你怎么一直看着我，是要和我一起刷题吗？",
        motion: "Tap嘴"
      },
      {
        text: "AC啦！Accept！恭喜恭喜！",
        motion: "Tap左眼",
        from: {
          "Part15": 1
        },
        to: {
          "Part15": 0
        }
      }
    ]
    canvas.width = model.width * 1.2
    const hideParts = [
      "Part5", // 晕
      "neko", // 喵喵拳
      "game", // 左手游戏手柄
      "Part15", // 墨镜
      // "Part21", // 右手小臂
      // "Part22", // 左手垂下
      "gitar", // 吉他 ！和 上面 part21 22 冲突
      "Part", // 双手抱拳
      "Part16", // 惊讶特效
      "Part12" // 小心心
    ]
    const hidePartsIndex = hideParts.map(id => coreModel._partIds.indexOf(id))
    hidePartsIndex.forEach(idx => {
      coreModel._partOpacities[idx] = 0
    })
  }
}


var pio_reference
window.onload = updateGod
