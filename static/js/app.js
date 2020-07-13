document.addEventListener("DOMContentLoaded", async () => {
    var short_button = document.getElementById("btn_short");
    var expiring_button = document.getElementById("btn_10min");
    var one_off_button = document.getElementById("btn_one_off");
    var link_src = document.getElementById("link_src");
    var link_result = document.getElementById("link_result");
    var result_block = document.getElementById("result");

    const create_link = async (args={}) => {
        const response = await fetch('/links/', {
            method: 'POST',
            body: JSON.stringify(Object.assign(args, {
                'src': link_src.value
            })),
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (response.status == 201) {
            const jsonResp = await response.json();

            link_result.innerText = window.location.origin + '/' + jsonResp['short'];
            result_block.style.display = 'block';
        } else {
            alert("Произошла ошибка при отправке запроса, проверьте правильность ввода ссылки.");
        }
    }

    short_button.onclick = async () => {
        await create_link();
        return false;
    }

    one_off_button.onclick = async() => {
        await create_link({'is_one_off': true});
        return false;
    }

    expiring_button.onclick = async () => {
        await create_link({'expiring': true});
        return false
    }
});