let expense_record_btn = document.getElementById('expense-record')

expense_record_btn.addEventListener('click', (e)=>{
    const page_url='/pft/expense-record/page'
    fetch(page_url, {
        method: 'POST',
        headers: { 'Accept': 'text/html' },
    }).then( res => res.text()).then(html => {
        console.log(html)
        document.querySelector('#main-content').innerHTML = html;
    })
})