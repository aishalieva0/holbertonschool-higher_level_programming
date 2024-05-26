const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

async function sayHelloInFrench() {
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(res.status);
    const { hello } = await res.json();
    const helloElement = document.getElementById('hello').textContent = hello;

  } catch (e) {
    console.log('Error', e)
  }
};

sayHelloInFrench();