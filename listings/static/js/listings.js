$(document).on('click', '.confirm-delete', function(){
  return confirm('Are you sure you want to delete this?');
})

$(document).on('click', '.reset', function(){
  console.log('hola');
  return window.history.back();
})
