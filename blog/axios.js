import axios from 'axios'

// Pega a variável definida no ambiente, ou usa localhost como fallback
const apiBaseURL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/'

const api = axios.create({
  baseURL: apiBaseURL
})

api.interceptors.request.use(config => {
  const token = localStorage.getItem('accessToken')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default api
// Exemplo de uso
