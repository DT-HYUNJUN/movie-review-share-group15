const ratings = document.querySelectorAll('#rating')

ratings.forEach(rating => {
  
  console.log(rating.textContent)
  if (rating.textContent > 60) {
    rating.classList.add('bg-success')
  } else if (rating.textContent > 40) {
    rating.classList.add('bg-warning')
  } else {
    rating.classList.add('bg-danger')
  }
});
