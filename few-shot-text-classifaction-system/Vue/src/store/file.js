import axios from 'axios'

export function download_file(data, file_name) {
    const url = 'http://127.0.0.1:5000/send'
    const config = {
        responseType: 'arraybuffer',
        headers: {
            "X-TOKEN": "xxx"
        }
    }
    axios.post(url, data, config).then(
        resp => {
            const blob = new Blob([resp.data])
            const link = document.createElement('a')
            link.download = file_name // a标签添加属性
            link.style.display = 'none'
            link.href = URL.createObjectURL(blob)
            document.body.appendChild(link)
            link.click() // 执行下载
            URL.revokeObjectURL(link.href)  // 释放 bolb 对象
            document.body.removeChild(link) // 下载完成移除元素
        }).catch(function (error) {
        console.log(error)
    })
}
