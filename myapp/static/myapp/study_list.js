// study_list.js

function appendStudyItem(title, url, content) {
    // 동적으로 리스트 아이템 추가하는 코드
}

// Django에서 전달한 데이터를 HTML의 data 속성을 통해 추출
var a_titlelist = JSON.parse(document.getElementById('studyListData').getAttribute('data-a-titlelist'));
var a_urllist = JSON.parse(document.getElementById('studyListData').getAttribute('data-a-urllist'));
var contentlist = JSON.parse(document.getElementById('studyListData').getAttribute('data-contentlist'));

// 리스트 아이템 추가
for (var i = 0; i < a_titlelist.length; i++) {
    appendStudyItem(a_titlelist[i], a_urllist[i], contentlist[i]);
}