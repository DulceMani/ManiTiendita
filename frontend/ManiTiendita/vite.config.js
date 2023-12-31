import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    
     host: true,
     strictPort: true,
     port: 3001, // This is the port which we will use in docker,
     //hmr: { host: 'localhost', },
    watch: {
      usePolling: true,
    },
  }
})
