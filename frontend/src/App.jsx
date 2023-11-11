import { FormThemeProvider } from 'react-form-component'
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom'
import ScannedDisplay from './components/ScannedDisplay'
import './App.css'
import MyFormComponent from './components/MyFormComponent'

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<FormThemeProvider><MyFormComponent/></FormThemeProvider>} />
        <Route path="/results" element={<ScannedDisplay></ScannedDisplay>} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
