// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import { md } from 'vuetify/iconsets/md'

// Vuetify
import { createVuetify } from 'vuetify'

export default createVuetify({
  icons: {
    iconfont: 'md',
    values: {
      md,
    },
    theme: {
      primary: "#9652ff",
      sucess: "#3cdic2",
      info: "#ffaa2c",
      error: "#f83e70"
    }
  },
  })