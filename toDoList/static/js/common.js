// 获取cookie
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function del_thing(id) {
    var url = 'edit/' + id;
    $.ajax({
        url: url,
        type: 'DELETE',
        async: false,
        headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                },
        // responseType: 'json',
        success: function (data) {
            if(data.code == '1') {
                location.href = '/'
            }else {
                alert('delete fail')
            }

        }
    })
}