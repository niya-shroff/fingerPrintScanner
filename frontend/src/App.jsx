import { FormThemeProvider } from 'react-form-component'
import InputForm from './components/InputForm'
import './App.css'

function App() {
  return (
    <FormThemeProvider>
      <InputForm />
  </FormThemeProvider>
  )
}

export default App