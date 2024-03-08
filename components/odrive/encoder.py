from enums import EncoderError, Error, EncoderMode


class Encoder(Error):
    """
    ODrive encoder abstract class

    Full document:
    https://docs.odriverobotics.com/v/0.5.4/fibre_types/com_odriverobotics_ODrive.html#ODrive.Encoder

    This class is not included all configurations from the document
    """

    def __init__(self, encoder) -> None:
        self.encoder = encoder
        # https://docs.odriverobotics.com/v/0.5.4/fibre_types/com_odriverobotics_ODrive.html#ODrive.Encoder.Error
        self.error: int = encoder.error

    def get_errors(self) -> str:
        """
        Return encoder errors
        """
        # https://docs.odriverobotics.com/v/0.5.4/fibre_types/com_odriverobotics_ODrive.html#ODrive.Encoder.Error
        errors = self.decode_errors(self.encoder.error)
        return " & ".join([EncoderError(error).name for error in errors])

    def is_ready(self) -> str:
        # https://docs.odriverobotics.com/v/0.5.4/fibre_types/com_odriverobotics_ODrive.html#ODrive.Encoder.is_ready
        return self.decode_status(self.encoder.is_ready)

    def index_found(self) -> str:
        # https://docs.odriverobotics.com/v/0.5.4/fibre_types/com_odriverobotics_ODrive.html#ODrive.Encoder.index_found
        return self.decode_status(self.encoder.index_found)

    def set_configs(self) -> None:
        """
        Full document: https://docs.odriverobotics.com/v/0.5.4/fibre_types/com_odriverobotics_ODrive.html#ODrive.Encoder.Config
        """
        # https://docs.odriverobotics.com/v/0.5.4/fibre_types/com_odriverobotics_ODrive.html#ODrive.Encoder.Mode
        self.encoder.config.mode = EncoderMode.HALL
        # https://docs.odriverobotics.com/v/0.5.4/fibre_types/com_odriverobotics_ODrive.html#ODrive.Encoder.Config.cpr
        self.encoder.config.cpr = 42
        # https://docs.odriverobotics.com/v/0.5.4/fibre_types/com_odriverobotics_ODrive.html#ODrive.Encoder.Config.bandwidth
        self.encoder.config.bandwidth = 100
        # https://docs.odriverobotics.com/v/0.5.4/fibre_types/com_odriverobotics_ODrive.html#ODrive.Encoder.Config.calib_scan_distance
        self.encoder.config.calib_scan_distance = 100
        # https://docs.odriverobotics.com/v/0.5.4/fibre_types/com_odriverobotics_ODrive.html#ODrive.Encoder.Config.calib_scan_omega
        self.encoder.config.calib_scan_omega = 50
