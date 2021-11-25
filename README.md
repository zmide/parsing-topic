# parsing-topic

## 使用前你需要了解的 🔍

> 目前解析的样式比较少，所有不能够将所有类型题目全部解析( 目前支持的题目类型：选择题、判断题、填空题 ) ,最建议的题目格式如下：

```
选择题
1.大学体育工作中的（ A ），主要是通过组织学生进行体育课学习、体育竞赛活动和各种身体锻炼来实现的，寓教育于身体活动之中。
A、思想教育  
B、体育锻炼能力   
C、心理素质教育    
D、体育技能教育
2.大学体育工作中的（  ），主要是通过组织学生进行体育课学习、体育竞赛活动和各种身体锻炼来实现的，寓教育于身体活动之中。
A、思想教育  
B、体育锻炼能力   
C、心理素质教育    
D、体育技能教育
答案：A

判断题
1.体育锻炼可以增强抵抗力和免疫能力，从而减少癌症的发生。	（√）
2.体育锻炼可以增强抵抗力和免疫能力，从而减少癌症的发生。	答案：对
```

>  如果你的题目样式不在其中，也不要担心，请联系QQ群 `964722860` 中的群主或管理员，我们会尽快添加适配。

最后感谢您的支持，我们更新的动力离不开您的支持与鼓励。🎉

全能搜题官网：<https://so.jszkk.com>

全能搜题 App 开源 GitHub 项目地址：<https://github.com/PBK-B/chaoxing-tool-client>

> 注: 全能搜题全部开源项目遵从 [MIT 许可协议开源](https://github.com/zmide/study.zmide.com/blob/main/LICENSE) ，任何人可以将其任意代码用于任何地方

> 免责声明: 受项目公开性质，作者以贡献者们不能保证数据来源是否合规，任何人都能提交搜索和使用系统的全部数据，在您使用该项目的任何服务时必须遵守相关国家法律法规并且本系统的全部文字在[知识共享 署名-相同方式共享 3.0 协议](https://creativecommons.org/licenses/by-sa/3.0/cn/deed.zh)之条款下提供，附加条款亦可能应用。（请参阅[使用条款](https://creativecommons.org/licenses/by-sa/3.0/cn/deed.zh)）

## 目录结构 🔧

```
├── app                		# 整个项目的入口
├── clear              		# 文件清洗库
  	├── main		   		  # 文件清洗的入口
  	├── startRun	   		# 文件清洗的框架
  	├── clearTopic	   	# 文件清洗的具体实现
  	├── tools		   		  # 工具库
  	├── conf		   		  # 配置
└── blueprint          		# 蓝图模块
    ├── appBlueprint   		# 路由
    ├── encapsulateResult   # 封装返回结果
└── logs					# 日志文件
└── data					# 存放解析数据
└── tmpdata					# 存放临时文件
```

## 目前提供的API ⚒️

### 单题解析

> 说明 : 调用此接口 , 可将解析单个题目(直接输入题目内容)

**接口类型**:	`post`

**必选参数**:	`content`：题目内容

**接口地址**:	`/parsing`



### 文件解析

> 说明 : 调用此接口 , 可解析文件内容(目前只支持TXT,小伙伴们可以将word转为TXT之后尝试)

**接口类型**:	`post`

**必选参数**:	`file`：文件

**接口地址**:	`/parsingFile`



### 获取日志

>  说明:  解析题目放回的结果中会有 `logId` , 可以通过 `logId` 查看解析中出现了什么问题

**接口类型**:	`get`

**必选参数**:	`logId`：日志Id

**接口地址**:	`/errorLog`



### 获取解析内容

>  说明:  调用此接口将获得一个解析完之后的json文件

**接口类型**:	`get`

**必选参数**:	`dataId`：日志Id

**接口地址**:	`/getResultData`



# 解析之后的数据结构 🎉

```json
 {
     // type 题目类型 0 单选题 1 => 多选题 3=> 判断题
     "type": 0,
     // id 题目ID
     "id": 0,
     // name  题目类型
     "name": "单选题",
     // content  题干
     "content": "阴阳的最初含义是指",
     // answer  题目答案部分
     "answer": [
         {
             // name 选项名称
             "name": "A",
             // content 选项内容
             "content": "天地日月",
             // isanswer 选项结果
             "isanswer": false
         },
         {
             "name": "B",
             "content": "动静变化",
             "isanswer": false
         },
         {
             "name": "C",
             "content": "昼夜节律",
             "isanswer": false
         },
         {
             "name": "D",
             "content": "日光向背",
             "isanswer": true
         },
         {
             "name": "E",
             "content": "上下升降",
             "isanswer": false
         }
     ]
}
```




## QA 💡

Q: 我能使用该项目或者项目的搜题接口去做商业项目或者毕业设计吗？

> A: 全能搜题项目全部开源项目都是基于 MIT license 开源协议，你可以将其使用在任何地方没有任何限制。

Q: 想学习技术？

> A: 我们欢迎大家加入一起维护系统，网站，脚本等。有 Python，JavaScript，PHP，Java，Kotlin，Golang… 编程语言基础的都能在我们这里学习到以下技术：网站搭建，前端 React and Vue 技术，前端网站架构，后端 Laravel 框架，Python 数据处理，Android MVVM App 架构…（如果您还没任何编程语言基础的话可以先去选择一门编程语言学习基础，希望我们一起学习进步，与君共勉。）

## License
