//Step 1: enter into javascript console on google image search page
//finds thumbnail image links that open detailed view and saves links to file

im = document.getElementsByClassName("rg_l");
string = [].map.call( im, function(node){
        return node.href || node.textContent || node.innerText || "";
}).join(",");
window.open('data:text/csv;charset=utf-8,' + escape(string));