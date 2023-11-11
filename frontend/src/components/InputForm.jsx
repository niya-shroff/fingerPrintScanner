import Form, {Input, Select, FormButton} from 'react-form-component'
import SendFormData from './SendFormData'

const InputForm = () =>
  <Form fields={['name', 'email', 'type']}>
    <Input
      name='name'
      label='User name'
    />
    <Input
      name='email'
      type='email'
      label='E-mail'
    />
    <Select
      name='type'
      label='Type of a user'
      options={['Viewer', 'Moderator', 'Admin']}
    />
    <FormButton
      onClick={data => 
        SendFormData(data)
      }
    >Save</FormButton>
  </Form>

export default InputForm