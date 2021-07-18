import request from "request";

function requestPost(url, requestData) {
    request({
        url: url,
        method: "POST",
        json: true,
        headers: {
            "content-type": "application/json",
        },
        body: JSON.stringify(requestData)
    },
        function (error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log("responseData: ", body) // 请求成功的处理逻辑
        }
    });
}

export default requestPost;