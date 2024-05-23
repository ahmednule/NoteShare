// Styles
import '@fortawesome/fontawesome-free/css/all.css';
import '@mdi/font/css/materialdesignicons.css';
import {aliases, fa} from 'vuetify/iconsets/fa';
import 'vuetify/styles';
import { createVuetify } from 'vuetify';

// Vuetify
import { createVuetify } from 'vuetify'

export default createVuetify(
 {
  icons: {
    defaultSet: 'fa',
    aliases,
    sets: {
      fa,
    },
  },
 });
