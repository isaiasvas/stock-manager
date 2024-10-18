(function($) {
    $(document).ready(function() {
        function calcularTotal() {
            console.log('Função calcularTotal chamada'); // Para verificar se a função está sendo chamada
            let total = 0;
            $('table#id_itens tbody tr').each(function() {
                const quantidade = parseFloat($(this).find('input[name$=quantidade]').val()) || 0;
                const preco = parseFloat($(this).find('select[name$=produto] option:selected').data('preco')) || 0;
                console.log(`Quantidade: ${quantidade}, Preço: ${preco}`); // Para verificar os valores
                total += quantidade * preco;
            });
            $('#id_valor_total').val(total.toFixed(2));
        }
        

        // Chama a função ao mudar a quantidade ou o produto
        $('table#id_itens').on('change', 'input[name$=quantidade], select[name$=produto]', calcularTotal);
    });
})(django.jQuery);
