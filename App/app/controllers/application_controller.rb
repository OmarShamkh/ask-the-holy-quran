class ApplicationController < ActionController::Base
    before_action :set_query
    include Pagy::Backend

    def set_query
      @query = Aya.ransack(params[:q])
    end

end
