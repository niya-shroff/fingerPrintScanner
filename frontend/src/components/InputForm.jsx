import Form, { Input, FormButton } from 'react-form-component';
import SendFormData from './SendFormData';

const InputForm = () => {

  return (
    <Form fields={['firstName', 'lastName', 'email', 'spire']}>
      <Input
        name='firstName'
        type='name'
        label='First Name'
      />
      <Input
        name='lastName'
        type='name'
        label='Last Name'
      />
      <Input
        name='email'
        type='email'
        label='E-mail Address'
      />
      <Input
        name='spire'
        type='number'
        label='Spire ID'
      />
      <FormButton
        onClick={data => {
          SendFormData(data)
        }
        }
      >Save</FormButton>
    </Form>
  )
}

export default InputForm