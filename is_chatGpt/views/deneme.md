

<?xml version="1.0" encoding="utf-8"?>
<odoo>
	<data>
		<!-- Görünüm Tanımı -->
		<record id="view_chatgpt_model_form" model="ir.ui.view">
			<field name="name">
				chatGPTview.form
			</field>
			<field name="model">
				chatgpt.model
			</field>
			<field name="arch" type="xml">
				<form string="ChatGPT Model">
					<field name="user_input" />
					<field name="output_message" />
					<button name="send_user_input" string="Generate Response" type="object" class="btn-primary" />
				</form>
			</field>
		</record>
	</data>
</odoo>
