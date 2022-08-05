class TafseersController < ApplicationController
  def show
    @tafser = Tafseer.find(params[:id])
    render 'show'

  end

  def index
    @tafseers = Tafseer.all.order(:id)
    render 'index'
  end
end
