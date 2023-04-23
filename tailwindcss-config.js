/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.{html,js}"],
  theme: {
    fontFamily: {
      'Poppins': ['poppins', 'serif'],
      'Quicksand': ['quicksand', 'serif']
    },
    screens: {
      '2xl': '1536px',
      'xl': '1280px',
      'lg': '1024px',
      'mmd': '986px',
      'md': '768px',
      'sm': '576px',
      'xs': '480px',
      'xxs': '320px'
    },
    extend: {},
  },
  plugins: [],
}
