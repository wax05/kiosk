const monja = [
    {
        type: 's',
        title: "횡단을 하려면 6일 걸리는 사막을 가려는 탐험가가있다.한사람이 가져갈수있는 식량은 4일치, 몇명의 짐꾼을 데려가야할까?",
        dab: ["2명"]
    },
    {
        type: 's',
        title: "컴퓨터가 최초로 한국에 들어온 연도는?",
        dab: ["1961년","1961"]
    },
    {
        type: 's',
        title: "(1+sinx)/n=?",
        dab: ["7"]
    },
    {
        type: 's',
        title: "컴퓨터에서 정보의 기본 단위",
        dab: ["byte"]
    },
    {
        type: 's',
        title: "프로그램을 간결하게 쓸 수 있고, 프로그래밍하기 쉽고 편리한 언어는 무엇일까요? ",
        dab: ["C언어"]
    },
    {
        type: 's',
        title: "컴퓨터 프로그램을 작성하는 일은 무엇이라고 하나요? ",
        dab: ["프로그래밍"]
    },
    {
        type: 's',
        title: "1GB(기가바이트)는 몇 MB(메가바이트)와 같은가요? ",
        dab: ["1024"]
    },
    {
        type: 's',
        title: "C언어가 만들어진 년도는 언제인가요? ",
        dab: ["1971년","1971"]
    },
    {
        type: 's',
        title: "기계(컴퓨터)에게 명령이나 연산을 시킬 목적으로 설계되어 기계와 의사소통을 할 수 있게 해주는 언어는? ",
        dab: ["프로그래밍언어"]
    },
    {
        type: 's',
        title: "썬 마이크로시스템즈에서 1995년에 개발한 객체 지향형 프로그래밍 언어는?",
        dab: ["자바","java","Java","JAVA"]
    },
    {
        type: 'OX',
        title: "오늘이 내일이면 좋겠다 그러면 오늘이 금요일일 땐데 오늘은 일요일이다.",
        dab: "O"
    },
    {
        type: 'OX',
        title: "C언어는 B언어를 개선하여 만들었다",
        dab: "O"
    },
    {
        type: 'OX',
        title: "현재 사용되는 대부분의 언어는 c언어에서 파생되었다",
        dab: "O"
    },
    {
        type: 'OX',
        title: "python은 c언어에서 파생된언어이다",
        dab: "O"
    },
    {
        type: 'OX',
        title: "윈도우는 자바로 만들어졌다",
        dab: "O"
    },
    {
        type: 'OX',
        title: "기계어와 구분하기 위해 인간이 일상생활에서 의사 소통을 위해 사용하는 언어를 가리키는 말을 자연어라고 한다.",
        dab: "O"
    },
    {
        type: 'OX',
        title: "C#은 프로그래밍 언어이다.다",
        dab: "O"
    },
]

let nowmonja = {
    type:'',
    title:'',
    dab:''
}

let LeftAttempt = 3

const title = document.querySelector('.title');
const dab = document.querySelector('.dab');
const make_btn = document.querySelector('#make');
const check_btn = document.querySelector('#check');

const input_contaienr = document.querySelector('.input-contaienr')
const add_input_contaiener = document.querySelector('#add-input-contaiener')

const html1 = `<div class="OX"><div class="O">O</div><div class="X">X</div></div>`
const html2 = `<input class="input">`

check_btn.style.display = 'none'

make_btn.addEventListener('click', () => {
    make_btn.style.display = 'none'
    const mon = monja[Math.floor(Math.random() * monja.length)]
    console.log(mon)
    nowmonja.type = mon.type
    nowmonja.title = mon.title
    nowmonja.dab = mon.dab

    if(nowmonja.type === 's'){
        add_input_contaiener.innerHTML = html2
        check_btn.style.display = 'block'
    }else if(nowmonja.type === 'OX'){
        add_input_contaiener.innerHTML = html1
        const O = document.querySelector('.O')
        const X = document.querySelector('.X')

        O.addEventListener('click', () => {
    if(nowmonja.dab === 'O'){
        alert('정답입니다!');
        d()
    } else {
        if (LeftAttempt > 1) {
            console.log(LeftAttempt)
            alert(`정답이 아닙니다.${LeftAttempt}번의 기회가 남았습니다`);
            LeftAttempt --;
        } else {
            alert("정답이 아닙니다");
            d();
            LeftAttempt = 3;
        }
    }
})

X.addEventListener('click', (e) => {
    if(nowmonja.dab === 'X'){
        alert('정답입니다!');
        d();
    } else{
        if (LeftAttempt > 1) {
            LeftAttempt --;
            alert(`정답이 아닙니다.${LeftAttempt}번의 기회가 남았습니다`);
        } else {
            alert("정답이 아닙니다");
            d();
            LeftAttempt = 3;
        }
    }
})
    }

    title.innerHTML = mon.title
})

check_btn.addEventListener('click', () => {
    
    if(nowmonja.type === 's'){
        check_btn_f()
    }else if(nowmonja.type === 'OX'){
        check_btn_f()
    }
})

function check_btn_f() {
    const input = document.querySelector('.input');
    let TF_Check = null;
    if(input.value === ''){
        alert('답을 입력해 주세요');//공백체크
    } else {
        nowmonja.dab.forEach(ForElement => {
            if (input.value !== '' && input.value === ForElement) {
            TF_Check = true;
            }
        });
        if(TF_Check !== null) {
            add_input_contaiener.innerHTML = ''
            check_btn.style.display = 'none'
            make_btn.style.display = 'block'
            title.innerHTML = '이부분에 문제가 표시 됩니다. <br> "문제 만들기" 버튼을 눌러주세요.'
            alert('정답입니다!')
        } else {
            if (LeftAttempt > 1) {
            LeftAttempt --;
                alert(`정답이 아닙니다.${LeftAttempt}번의 기회가 남았습니다`);
            } else {
                alert("정답이 아닙니다");
                LeftAttempt = 3;
                add_input_contaiener.innerHTML = ''
                check_btn.style.display = 'none'
                make_btn.style.display = 'block'
                title.innerHTML = '이부분에 문제가 표시 됩니다. <br> "문제 만들기" 버튼을 눌러주세요.'
            }
        }
    }
}

function d() {
    add_input_contaiener.innerHTML = ''
    check_btn.style.display = 'none'
    make_btn.style.display = 'block'
    title.innerHTML = '이부분에 문제가 표시 됩니다. <br> "문제 만들기" 버튼을 눌러주세요.'
}