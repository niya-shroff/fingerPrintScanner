import { FormThemeProvider } from 'react-form-component'
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom'
import Results from './components/Results'
import MyFormComponent from './components/MyFormComponent'
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<FormThemeProvider><MyFormComponent/></FormThemeProvider>} />
        <Route path="/results" element={<Results></Results>} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App