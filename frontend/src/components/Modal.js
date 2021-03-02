import React, { Component } from "react";
    import {
      Button,
      Modal,
      ModalHeader,
      ModalBody,
      ModalFooter,
      Form,
      FormGroup,
      Input,
      Label
    } from "reactstrap";

    export default class CustomModal extends Component {
      constructor(props) {
        super(props);
        this.state = {
          activeItem: this.props.activeItem
        };
      }
      handleChange = e => {
        let { name, value } = e.target;
        if (e.target.type === "checkbox") {
          value = e.target.checked;
        }
        const activeItem = { ...this.state.activeItem, [name]: value };
        this.setState({ activeItem });
      };
      render() {
        const { toggle, onSave } = this.props;
        return (
          <Modal isOpen={true} toggle={toggle}>
            <ModalHeader toggle={toggle}> Produto </ModalHeader>
            <ModalBody>
              <Form>
                <FormGroup>
                  <Label for="description">Descrição</Label>
                  <Input
                    type="text"
                    name="descricao"
                    value={this.state.activeItem.descricao}
                    onChange={this.handleChange}
                    placeholder="Descrição do produto"
                  />
                </FormGroup>
                <FormGroup>
                  <Label for="description">Data de validade</Label>
                  <Input
                    type="date"
                    name="data_validade"
                    value={this.state.activeItem.data_validade}
                    onChange={this.handleChange}
                    placeholder="__/__/____"
                  />
                </FormGroup>
                <FormGroup>
                  <Label for="description">Quantidades/Unid em estoque</Label>
                  <Input
                    type="text"
                    name="qtd_estoque"
                    value={this.state.activeItem.qtd_estoque}
                    onChange={this.handleChange}
                    placeholder="Quantidade em estoque"
                  />
                </FormGroup>
                <FormGroup>
                  <Label for="description">Preço da Unidade</Label>
                  <Input
                    type="text"
                    name="preco_unid"
                    value={this.state.activeItem.preco_unid}
                    onChange={this.handleChange}
                    placeholder="Preço da unidade do produto"
                  />
                </FormGroup>
              </Form>
            </ModalBody>
            <ModalFooter>
              <Button color="success" onClick={() => onSave(this.state.activeItem)}>
                Salvar
              </Button>
            </ModalFooter>
          </Modal>
        );
      }
    }