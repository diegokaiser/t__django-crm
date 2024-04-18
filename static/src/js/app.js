const app = []

app.home = {
  init: () => {
    console.log(':)')
  },
  search: () => {
    const onClickSearchByProduct = document.querySelector('.js-searchByProduct')
    const onClickSearchByKeyword = document.querySelector('.js-searchByKeyword')
    const searchByProduct = document.querySelector('.search__byProduct')
    const searchByKeyword = document.querySelector('.search__byKeyword')

    onClickSearchByProduct.addEventListener('click', (event) => {
      onClickSearchByProduct.classList.add('active')
      onClickSearchByKeyword.classList.remove('active')
      searchByProduct.classList.add('active')
      searchByKeyword.classList.remove('active')
    })
    onClickSearchByKeyword.addEventListener('click', (event) => {
      onClickSearchByKeyword.classList.add('active')
      onClickSearchByProduct.classList.remove('active')
      searchByProduct.classList.remove('active')
      searchByKeyword.classList.add('active')
    })
  }
}
window.addEventListener('load', () => {
  app.home.init()
  app.home.search()
})

