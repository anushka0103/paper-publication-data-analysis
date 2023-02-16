function valid() {
  //validating author name

  for (i = 0; i < Author.length; i++) {
    ch = Author.charAt(i)
    if (
      !(ch >= 'a' && ch <= 'z') &&
      !(ch >= 'A' && ch <= 'Z') &&
      !(ch == ' ')
    ) {
      alert('Invalid Author')
    }
  }

  //validating year
  var Year = document.getElementById('Year').value
  if (isNaN(Year)) {
    alert('Year given is invalid')
  }

  //validating domain name
  var Domain = document.getElementById('Domain').value
  for (i = 0; i < Domain.length; i++) {
    ch = Domain.charAt(i)
    if (
      !(ch >= 'a' && ch <= 'z') &&
      !(ch >= 'A' && ch <= 'Z') &&
      !(ch == ' ')
    ) {
      alert('Invalid Domain')
    }
  }

  return true
}
