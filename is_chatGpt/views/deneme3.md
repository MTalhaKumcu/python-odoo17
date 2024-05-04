<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <!-- Model Tanımı -->
        <record id="model_chatgpt_model" model="ir.model">
            <field name="name">ChatGPT Model</field>
            <field name="model">chatgpt.model</field>
          <!--    <field name="description">ChatGPT Model</field>-->
        </record>

        <!-- Görünüm Tanımı -->
        <record id="view_chatgpt_model_form" model="ir.ui.view">
            <field name="name">chatgpt.model.form</field>
            <field name="model">chatgpt.model</field>
            <field name="arch" type="xml">
                <form string="ChatGPT Model">
                    <sheet>
                        <group>
                            <field name="name"/>
                            <field name="user_input"/>
                            <field name="output_message"/>
                        </group>
                        <footer>
                            <button name="send_user_input" string="Generate Response" type="object" class="btn-primary"/>
                        </footer>
                    </sheet>
                </form>
            </field>
        </record>
    </data>
</odoo>
