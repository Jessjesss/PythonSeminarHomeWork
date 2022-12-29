import logger
import view
import model


def run():
    while True:
        mode = view.choose_mode()
        if mode == '1':
            record = view.record_number()
            logger.rec_data(record)
        elif mode == '2':
            record = view.cont_to_s()
            base = logger.get_data()
            result = model.search_data(base, record)
            view.print_result(result)